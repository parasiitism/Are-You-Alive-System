from sqlalchemy.orm import Session
from .models import User

def get_user_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phone_primary == phone).first()

def create_user(db: Session, user_data):
    user = User(
        phone_primary=user_data.phone_primary,
        phone_emergency=user_data.phone_emergency,
        consent_given=user_data.consent_given
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
