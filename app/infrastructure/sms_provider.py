import requests
from app.config import ENV, MSG91_AUTH_KEY, MSG91_TEMPLATE_ID


def send_sms(phone: str, otp: str) -> None:
    """
    Sends OTP using MSG91 in PROD
    Prints OTP in DEV
    """

    if ENV != "PROD":
        print(f"[DEV SMS] OTP for {phone}: {otp}")
        return

    url = "https://api.msg91.com/api/v5/otp"

    payload = {
        "authkey": MSG91_AUTH_KEY,
        "template_id": MSG91_TEMPLATE_ID,
        "mobile": phone,
        "otp": otp
    }

    response = requests.post(url, json=payload, timeout=5)

    if response.status_code != 200:
        print("❌ MSG91 ERROR:", response.text)
