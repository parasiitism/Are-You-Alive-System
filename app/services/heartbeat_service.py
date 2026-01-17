from datetime import datetime

# Temporary in-memory store (later Redis / DB)
HEARTBEAT_STORE = {}


class HeartbeatService:

    @staticmethod
    def record(user_id: str):
        HEARTBEAT_STORE[user_id] = datetime.utcnow()

    @staticmethod
    def last_seen(user_id: str):
        return HEARTBEAT_STORE.get(user_id)
