from app.infrastructure.notifiers.base import Notifier
from app.domain.user import User

class EmailNotifier(Notifier):
    def send(self,user,message:str):
        print(f"📧 Email to {user.emergency_contact.email}: {message}")