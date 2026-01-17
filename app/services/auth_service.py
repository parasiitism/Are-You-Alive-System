from app.services.otp_service import OTPService


class AuthService:

    @staticmethod
    def send_otp(phone: str):
        OTPService.generate_and_send(phone)

    @staticmethod
    def verify_otp(phone: str, otp: str) -> bool:
        return OTPService.verify(phone, otp)
