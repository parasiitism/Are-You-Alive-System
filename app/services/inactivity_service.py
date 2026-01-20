from datetime import datetime, timedelta
from app.storage.activity_store import get_all_activity
from app.storage.user_store import get_user
from app.services.notification_service import notify_all

INACTIVITY_LIMIT = timedelta(hours=48)

def check_inactivity():
    now = datetime.utcnow()
    activity = get_all_activity()

    for user_id, last_alive in activity.items():
        if now - last_alive > INACTIVITY_LIMIT:
            user = get_user(user_id)
            if user:
                notify_all(
                    user,
                    "🚨 ALERT: User inactive for 48 hours"
                )
