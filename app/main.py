from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import auth, otp

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LifeCheck API")

app.include_router(auth.router)
app.include_router(otp.router)

@app.get("/")
def health():
    return {"status": "OK"}
