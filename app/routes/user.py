from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.emergency_content import EmergencyContact

router = APIRouter()   # ✅ NO PREFIX HERE

@router.post("/register")
def register_user(payload: dict, db: Session = Depends(get_db)):
    user_id = payload["user_id"]
    email = payload["email"]
    emergency_phone = payload["emergency_contact"]["phone"]

    user = User(
        id=user_id,
        email=email,
        phone=user_id
    )
    db.add(user)

    contact = EmergencyContact(
        user_id=user_id,
        phone=emergency_phone
    )
    db.add(contact)

    db.commit()

    return {"status": "user registered"}
