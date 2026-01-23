from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
import logging

from app.database import SessionLocal
from app.models.user import User
from app.models.emergency_content import EmergencyContact
from app.infrastructure.notifiers.factory import NotifierFactory

# --------------------------------------------------
# Logging configuration
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# --------------------------------------------------
# Alert repeat interval (hours)
# --------------------------------------------------
ALERT_REPEAT_HOURS = 1


def run():
    logger.info("🚀 Inactivity checker started")

    db: Session = SessionLocal()

    # Always use timezone-aware UTC
    now = datetime.now(timezone.utc)

    try:
        users = db.query(User).all()
        logger.info(f"Checking {len(users)} users for inactivity")

        for user in users:
            if not user.last_alive_at:
                continue

            # Convert DB time to UTC if needed
            last_alive = user.last_alive_at
            if last_alive.tzinfo is None:
                last_alive = last_alive.replace(tzinfo=timezone.utc)

            inactive_hours = (now - last_alive).total_seconds() / 3600

            # Not yet inactive
            if inactive_hours < user.alive_interval_hours:
                continue

            # How much time passed after allowed interval
            hours_overdue = inactive_hours - user.alive_interval_hours

            # Fire alerts only at repeat boundaries
            if int(hours_overdue) % ALERT_REPEAT_HOURS != 0:
                continue

            logger.warning(
                f"User {user.id} inactive for {int(inactive_hours)} hours"
            )

            contacts = (
                db.query(EmergencyContact)
                .filter(EmergencyContact.user_id == user.id)
                .order_by(EmergencyContact.priority)
                .all()
            )

          
            if not contacts:
                logger.warning(f"No emergency contacts for user {user.id}")
                continue

            for contact in contacts:
                print(f"Her is contact :{contact.phone}")
                print(f"Her is contact :{contact.email}")
                try:
                    if contact.phone:
                        NotifierFactory.get_notifier("sms").send(
                            to=contact.phone,
                            message=f"⚠️ {user.id} has been inactive."
                        )

                        NotifierFactory.get_notifier("call").send(
                            to=contact.phone,
                            message="Emergency alert"
                        )

                    if contact.email:
                        NotifierFactory.get_notifier("email").send(
                            to=contact.email,
                            message="User inactivity detected"
                        )

                except Exception as e:
                    logger.error(
                        f"Notification failed for user {user.id}: {e}"
                    )

    except Exception:
        logger.exception("❌ Inactivity checker failed")

    finally:
        db.close()
        logger.info("✅ Inactivity checker finished")


# --------------------------------------------------
# Entry point
# --------------------------------------------------
if __name__ == "__main__":
    run()
