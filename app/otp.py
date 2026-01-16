import random
from datetime import datetime, timedelta

OTP_STORE = {}

def generate_otp(phone: str):
    otp = str(random.randint(100000, 999999))
    OTP_STORE[phone] = {
        "otp": otp,
        "expires_at": datetime.utcnow() + timedelta(minutes=5)
    }
    print(f"[DEV OTP] {phone} -> {otp}")  # TEMP: console OTP
    return otp

def verify_otp(phone: str, otp: str):
    data = OTP_STORE.get(phone)

    if not data:
        return False

    if datetime.utcnow() > data["expires_at"]:
        return False

    return data["otp"] == otp
