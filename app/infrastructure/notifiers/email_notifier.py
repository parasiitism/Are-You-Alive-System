from app.infrastructure.notifiers.base import Notifier

class EmailNotifier(Notifier):
    def send(self,user_id:str,message:str):
        print(f"[EMAIL] to {user_id}:{message}")