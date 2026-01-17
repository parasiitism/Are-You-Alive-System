import random
from datetime import datetime, timedelta
from .sms_service import send_sms

OTP_STORE = {}

def generate_otp(phone: str):
    otp = str(random.randint(100000, 999999))

    OTP_STORE[phone] = {
        "otp": otp,
        "expires_at": datetime.utcnow() + timedelta(minutes=5)
    }

    message = f"Your LifeCheck OTP is {otp}. Valid for 5 minutes."
    send_sms(phone, message)

    return otp

def verify_otp(phone: str, otp: str):
    data = OTP_STORE.get(phone)

    if not data:
        return False

    if datetime.utcnow() > data["expires_at"]:
        return False

    return data["otp"] == otp
