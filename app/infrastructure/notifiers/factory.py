from app.infrastructure.notifiers.sms_notifier import SMSNotifier
from app.infrastructure.notifiers.email_notifier import EmailNotifier
from app.infrastructure.notifiers.call_notifier import CallNotifier

class NotificationFactory:

    @staticmethod
    def get_notifier(channel: str):
        if channel == "sms":
            return SMSNotifier()
        elif channel == "email":
            return EmailNotifier()
        elif channel == "call":
            return CallNotifier()
        else:
            raise ValueError("Unsupported notification channel")
