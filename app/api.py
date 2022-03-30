from fastapi import FastAPI
from app.common.controllers import user
from app.auth.controllers import auth

app = FastAPI(title="CRM API", version="0.0.1", description="API to crm app")


app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping", tags=["HealthCheck"])
async def pong():
    return {"ping": "pong!"}
