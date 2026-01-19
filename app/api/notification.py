from fastapi import APIRouter
from app.inactivity import InactivityEngine


router = APIRouter(prefix="/notify", tags=["Notification"])

@router.post("/run")
def run_notification_engine():
    InactivityEngine.run()
    return {"status": "notification engine executed"}
