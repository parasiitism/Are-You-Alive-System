import random
from datetime import datetime, timedelta
from app.storage.otp_store import OTPStore
from app.infrastructure.sms_provider import send_sms


class OTPService:
    OTP_EXPIRY_MINUTES = 5

    @staticmethod
    def generate_and_send(phone: str) -> None:
        otp = str(random.randint(100000, 999999))

        OTPStore.save(
            phone=phone,
            otp=otp,
            expires_at=datetime.utcnow() + timedelta(minutes=OTPService.OTP_EXPIRY_MINUTES)
        )

        send_sms(phone, otp)

    @staticmethod
    def verify(phone: str, otp: str) -> bool:
        data = OTPStore.get(phone)

        if not data:
            return False

        if datetime.utcnow() > data["expires_at"]:
            return False

        return data["otp"] == otp
