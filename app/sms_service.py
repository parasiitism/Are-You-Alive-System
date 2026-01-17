from .config import ENV, SMS_TEST_NUMBER

def send_sms(phone: str, message: str):
    if ENV == "DEV":
        print(f"[DEV SMS] To: {phone} | Message: {message}")
        return

    if phone != SMS_TEST_NUMBER:
        print(f"[BLOCKED SMS] Attempt to send to {phone}")
        return

    print(f"[PROD SMS SENT] To: {phone}")
