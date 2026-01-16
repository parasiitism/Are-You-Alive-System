from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LifeCheck API",
    description="Inactivity-based safety alert system"
)

app.include_router(auth.router)

@app.get("/")
def health():
    return {"status": "Backend running"}
