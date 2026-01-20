from app.infrastructure.notifiers.base import Notifier


class SMSNotifier(Notifier):
    def send(self,user,message:str):
        print(f"📩 SMS to {user.emergency_contact.phone}: {message}")