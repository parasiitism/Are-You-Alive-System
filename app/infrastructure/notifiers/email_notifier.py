from app.infrastructure.notifiers.base import Notifier

class EmailNotifier(Notifier):

    def send(self, to: str, message: str):
        print(f"📧 Email sent to {to}: {message}")
