from datetime import datetime, timedelta
from app.services.heartbeat_service import HEARTBEAT_STORE


# Configurable threshold
INACTIVITY_THRESHOLD_HOURS = 48


class InactivityEngine:
    """
    Detects users who have been inactive beyond threshold.
    """

    @staticmethod
    def find_inactive_users():
        inactive_users = []

        now = datetime.utcnow()
        threshold = now - timedelta(hours=INACTIVITY_THRESHOLD_HOURS)

        for user_id, last_seen in HEARTBEAT_STORE.items():
            if last_seen < threshold:
                inactive_users.append({
                    "user_id": user_id,
                    "last_seen": last_seen.isoformat()
                })

        return inactive_users
