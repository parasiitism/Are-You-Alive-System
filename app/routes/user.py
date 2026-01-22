from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.emergency_content import EmergencyContact
router = APIRouter()

@router.post("/register", status_code=201)
def register_user(payload: dict, db: Session = Depends(get_db)):
    """
    Registers a new user with emergency contact.
    """

    print("📥 Incoming registration payload:", payload)

    # ---- Extract payload safely ----
    try:
        user_id = payload["user_id"]          # phone or unique id
        email = payload["email"]
        emergency_phone = payload["emergency_contact"]["phone"]
        location_enabled = payload.get("location_enabled", False)
        alive_interval = payload.get("alive_interval_hours", 48)
    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required field: {str(e)}"
        )

    # ---- Check if user already exists ----
    existing_user = db.query(User).filter(User.id == user_id).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already registered"
        )

    # ---- Create User ----
    user = User(
        id=user_id,
        email=email,
        phone=user_id,
        location_enabled=location_enabled,
        alive_interval_hours=alive_interval
    )

    # ---- Create Emergency Contact ----
    emergency_contact = EmergencyContact(
        user_id=user_id,
        phone=emergency_phone
    )

    try:
        db.add(user)
        db.add(emergency_contact)
        db.commit()
    except Exception as e:
        db.rollback()
        print("❌ DB error:", e)
        raise HTTPException(status_code=500, detail="Failed to register user")

    print(f"✅ User registered successfully: {user_id}")

    return {
        "status": "success",
        "message": "User registered successfully",
        "user_id": user_id
    }
