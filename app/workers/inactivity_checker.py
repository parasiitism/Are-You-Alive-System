from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.models.emergency_contact import EmergencyContact
from app.infrastructure.notifiers.factory import NotifierFactory

def run():
    db: Session = SessionLocal()
    now = datetime.utcnow()

    users = db.query(User).all()

    for user in users:
        if now - user.last_alive_at > timedelta(hours=user.alive_interval_hours):
            contacts = (
                db.query(EmergencyContact)
                .filter(EmergencyContact.user_id == user.id)
                .order_by(EmergencyContact.priority)
                .all()
            )

            for contact in contacts:
                notifier = NotifierFactory.get_notifier("sms")
                notifier.send(
                    to=contact.phone,
                    message=f"⚠️ {user.id} has been inactive."
                )

                notifier = NotifierFactory.get_notifier("email")
                notifier.send(
                    to=contact.email,
                    message="User inactivity detected"
                )

                notifier = NotifierFactory.get_notifier("call")
                notifier.send(
                    to=contact.phone,
                    message="Emergency alert"
                )

    db.close()
