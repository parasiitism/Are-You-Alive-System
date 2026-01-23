from app.infrastructure.notifiers.sms_notifier import SMSNotifier
from app.infrastructure.notifiers.email_notifier import EmailNotifier
from app.infrastructure.notifiers.call_notifier import CallNotifier

class NotifierFactory:

    @staticmethod
    def get_notifier(channel: str):
        if channel == "sms":
            return SMSNotifier()
        if channel == "email":
            return EmailNotifier()
        if channel == "call":
            return CallNotifier()

        raise ValueError(f"Unsupported notification channel: {channel}")
