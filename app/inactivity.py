from datetime import datetime
from app.services.heartbeat_service import HEARTBEAT_STORE
from app.services.notification_service import NotificationService

INACTIVITY_THRESHOLD_HOURS = 48

class InactivityEngine:
    @staticmethod
    def run():
        now = datetime.utcnow()

        for user_id, last_seen in HEARTBEAT_STORE.items():
            inactive_hours = int(
                (now - last_seen).total_seconds() / 3600
            )

            if inactive_hours >= INACTIVITY_THRESHOLD_HOURS:
                NotificationService.notify(
                    user_id=user_id,
                    inactive_hours=inactive_hours
                )
