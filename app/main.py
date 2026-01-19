from fastapi import FastAPI
from app.api import auth, heartbeat, inactivity, notification
app = FastAPI(
    title="Are You Alive System",
    version="0.1.0"
)

app.include_router(auth.router)
app.include_router(heartbeat.router)
app.include_router(inactivity.router)      
app.include_router(notification.router)   

@app.get("/")
def health():
    return {"status": "ok"}
