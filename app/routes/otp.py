from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import User
from ..otp import generate_otp, verify_otp

router = APIRouter(prefix="/otp")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/send/{phone}")
def send_otp(phone: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone_primary == phone).first()
    if not user:
        raise HTTPException(404, "User not found")

    generate_otp(phone)
    return {"message": "OTP sent"}

@router.post("/verify")
def verify(phone: str, otp: str, db: Session = Depends(get_db)):
    if not verify_otp(phone, otp):
        raise HTTPException(400, "Invalid OTP")

    user = db.query(User).filter(User.phone_primary == phone).first()
    user.is_verified = True
    db.commit()

    return {"message": "Phone verified"}
