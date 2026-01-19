from app.infrastructure.notifiers.base import Notifier

class CallNotifier(Notifier):
    def send(self, user_id: str, message: str):
        print(f"[CALL] to {user_id}: {message}")
