from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes.user import router as user_router
from app.routes.alive import router as alive_router
from app.routes.location import router as location_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Are You Alive System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Are You Alive backend running"}

app.include_router(user_router, prefix="/user")
app.include_router(alive_router)
app.include_router(location_router)
