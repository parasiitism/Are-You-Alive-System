from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User

def check_inactive_users():
    db: Session = SessionLocal()

    now = datetime.utcnow()

    users = db.query(User).all()

    for user in users:
        if user.last_alive_at is None:
            continue

        deadline = user.last_alive_at + timedelta(hours=user.alive_interval_hours)

        if now > deadline:
            trigger_alert(user)

    db.close()


def trigger_alert(user: User):
    print(f"🚨 ALERT: User {user.id} inactive")

    # TODO:
    # 1. Send SMS
    # 2. Send Email
    # 3. Call emergency contact
