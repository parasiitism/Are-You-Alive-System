from app.infrastructure.notifiers.base import Notifier

class CallNotifier(Notifier):
    def send(self,user,message: str):
        print(f"📞 Calling {user.emergency_contact.phone}: {message}")
