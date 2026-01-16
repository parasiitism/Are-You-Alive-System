from datetime import datetime, timedelta

def is_user_inactive(user):
    delta = datetime.utcnow() - user.last_active_at
    return delta > timedelta(hours=user.inactive_threshold_hours)
