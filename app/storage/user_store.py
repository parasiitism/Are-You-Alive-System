USERS = {}

def save_user(user):
    USERS[user.user_id] = user

def get_user(user_id: str):
    return USERS.get(user_id)
