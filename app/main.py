from fastapi import FastAPI

from .database import engine
from .models import Base
from .routes import auth, otp, heartbeat


app = FastAPI(
    title="LifeCheck API",
    description="Inactivity-based safety alert system"
)

Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(otp.router)
app.include_router(heartbeat.router)


@app.get("/")
def health():
    return {"status": "OK"}
