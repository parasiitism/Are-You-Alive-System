from datetime import datetime

LAST_ALIVE = {}

def update_alive(user_id: str):
    LAST_ALIVE[user_id] = datetime.utcnow()

def get_last_alive(user_id: str):
    return LAST_ALIVE.get(user_id)

def get_all_activity():
    return LAST_ALIVE
