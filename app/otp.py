import random
from datetime import datetime, timedelta
from .sms_service import send_sms

OTP_STORE = {}

def generate_otp(phone: str):
    """
    Generates OTP, stores it temporarily, and sends it via SMS
    """

    otp = str(random.randint(100000, 999999))

    OTP_STORE[phone] = {
        "otp": otp,
        "expires_at": datetime.utcnow() + timedelta(minutes=5)
    }
    send_sms(phone, otp)

    return otp


def verify_otp(phone: str, otp: str):
    """
    Verifies OTP entered by user
    """

    data = OTP_STORE.get(phone)

    if not data:
        return False

    if datetime.utcnow() > data["expires_at"]:
        return False

    return data["otp"] == otp
