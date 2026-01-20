from fastapi import FastAPI
import asyncio

from app.routes.alive import router as alive_router
from app.routes.user import router as user_router
from app.services.inactivity_service import check_inactivity

app = FastAPI(title="Are You Alive")

app.include_router(user_router)
app.include_router(alive_router)

@app.on_event("startup")
async def startup():
    asyncio.create_task(inactivity_loop())

async def inactivity_loop():
    while True:
        check_inactivity()
        await asyncio.sleep(300)
