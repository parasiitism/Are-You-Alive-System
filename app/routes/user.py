from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import hashlib

from app.database import get_db
from app.models.user import User
from app.models.emergency_content import EmergencyContact

router = APIRouter()

@router.post("/register", status_code=201)
def register_user(payload: dict, db: Session = Depends(get_db)):
    print("📥 Incoming registration payload:", payload)

    try:
        user_id = payload["user_id"]
        email = payload["email"]
        password = payload["password"]
        emergency_phone = payload["emergency_contact"]["phone"]
        location_enabled = payload.get("location_enabled", False)
        alive_interval = payload.get("alive_interval_hours", 48)

        password_hash = hashlib.sha256(password.encode()).hexdigest()
    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required field: {str(e)}"
        )

    existing_user = db.query(User).filter(User.id == user_id).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already registered")

    user = User(
        id=user_id,
        email=email,
        phone=user_id,
        password_hash=password_hash,
        location_enabled=location_enabled,
        alive_interval_hours=alive_interval
    )

    try:
        db.add(user)
        db.commit()

        emergency_contact = EmergencyContact(
            user_id=user_id,
            phone=emergency_phone
        )

        db.add(emergency_contact)
        db.commit()

    except Exception as e:
        db.rollback()
        print("❌ DB error:", e)
        raise HTTPException(status_code=500, detail=str(e))

    print(f"✅ User registered successfully: {user_id}")

    return {
        "status": "success",
        "message": "User registered successfully",
        "user_id": user_id
    }


@router.post("/login")
def login_user(payload: dict, db: Session = Depends(get_db)):

    phone = payload.get("phone")
    password = payload.get("password")

    if not phone or not password:
        raise HTTPException(status_code=400, detail="Phone and password required")

    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if user.password_hash != password_hash:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "status": "success",
        "user_id": user.id,
        "email": user.email
    }
