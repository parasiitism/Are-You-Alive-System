from app.infrastructure.notifiers.base import Notifier

class SMSNotifier(Notifier):
    def send(self,user_id:str,message:str):
        # Later we can use here Twillo or MSG91
        print(f"[SMS] to {user_id}:{message}")