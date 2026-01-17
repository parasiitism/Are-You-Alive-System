class OTPStore:
    _store = {}

    @classmethod
    def save(cls, phone: str, otp: str, expires_at):
        cls._store[phone] = {
            "otp": otp,
            "expires_at": expires_at
        }

    @classmethod
    def get(cls, phone: str):
        return cls._store.get(phone)

    @classmethod
    def delete(cls, phone: str):
        cls._store.pop(phone, None)
