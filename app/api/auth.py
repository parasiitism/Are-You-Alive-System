from fastapi import APIRouter, HTTPException
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/send-otp/{phone}")
def send_otp(phone: str):
    AuthService.send_otp(phone)
    return {"message": "OTP sent"}


@router.post("/verify-otp")
def verify_otp(phone: str, otp: str):
    if not AuthService.verify_otp(phone, otp):
        raise HTTPException(status_code=400, detail="Invalid OTP")

    return {"message": "OTP verified"}
