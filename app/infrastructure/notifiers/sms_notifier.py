from app.infrastructure.notifiers.base import Notifier

class SMSNotifier(Notifier):

    def send(self, to: str, message: str):
        print(f"📩 SMS sent to {to}: {message}")
