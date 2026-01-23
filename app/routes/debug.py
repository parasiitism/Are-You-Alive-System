from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.emergency_content import EmergencyContact

router = APIRouter(prefix="/debug", tags=["Debug"])

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return [
        {
            "id": u.id,
            "email": u.email,
            "phone": u.phone,
            "last_alive_at": u.last_alive_at,
            "alive_interval_hours": u.alive_interval_hours,
            "location_enabled": u.location_enabled,
            "created_at": u.created_at
        }
        for u in users
    ]


@router.get("/contacts")
def get_all_contacts(db: Session = Depends(get_db)):
    contacts = db.query(EmergencyContact).all()

    return [
        {
            "id": c.id,
            "user_id": c.user_id,
            "name": c.name,
            "phone": c.phone,
            "email": c.email,
            "priority": c.priority
        }
        for c in contacts
    ]
