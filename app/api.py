from fastapi import FastAPI
from app.common.database import engine
from app.common.models.user import User


User.metadata.create_all(bind=engine)

app = FastAPI(title="CRM API", version="0.0.1", description="API to crm app")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping", tags=["HealthCheck"])
async def pong():
    return {"ping": "pong!"}
