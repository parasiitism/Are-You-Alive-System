import requests
from .config import ENV
import os

MSG91_AUTH_KEY = os.getenv("MSG91_AUTH_KEY")
MSG91_TEMPLATE_ID = os.getenv("MSG91_TEMPLATE_ID")

def send_sms(phone: str, otp: str):
    """
    Send OTP using MSG91 OTP API
    """

    if ENV != "PROD":
        print(f"[DEV SMS] OTP for {phone}: {otp}")
        return

    url = "https://api.msg91.com/api/v5/otp"

    payload = {
        "template_id": MSG91_TEMPLATE_ID,
        "mobile": phone,
        "authkey": MSG91_AUTH_KEY,
        "otp": otp
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        print("❌ MSG91 ERROR:", response.text)
    else:
        print("✅ OTP SENT VIA MSG91 TO", phone)
