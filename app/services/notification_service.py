from app.infrastructure.notifiers.factory import NotificationFactory

class NotificationService:

    @staticmethod
    def notify(user_id: str, inactive_hours: int):
        message = "We haven't heard from you. Please confirm you are safe."

        # Escalation rules
        if inactive_hours >= 96:
            channel = "call"
        elif inactive_hours >= 72:
            channel = "email"
        elif inactive_hours >= 48:
            channel = "sms"
        else:
            return  

        notifier = NotificationFactory.get_notifier(channel)
        notifier.send(user_id, message)
