from fastapi import FastAPI
from app.api import auth, heartbeat

app = FastAPI(title="Are You Alive System")

app.include_router(auth.router)
app.include_router(heartbeat.router)


@app.get("/")
def health():
    return {"status": "OK"}
