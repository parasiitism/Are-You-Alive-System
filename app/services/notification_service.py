from app.infrastructure.notifiers.factory import NotificationFactory
from app.domain.user import User

def notify_all(User,message:str):
    for notifier in NotificationFactory.get_notifier():
        notifier.send(User,message)