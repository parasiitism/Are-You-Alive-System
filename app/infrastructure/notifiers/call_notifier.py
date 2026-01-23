from app.infrastructure.notifiers.base import Notifier

class CallNotifier(Notifier):

    def send(self, to: str, message: str):
        print(f"📞 Call placed to {to}: {message}")
