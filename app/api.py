from fastapi import (FastAPI)
from app.common.controllers import user
from app.auth.controllers import auth
from app.common.controllers import reset_password
from app.common.controllers import quote
from app.common.controllers import item

app = FastAPI(title="CRM API", version="0.0.1", description="API to crm app")

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(reset_password.router)
app.include_router(quote.router)
app.include_router(item.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping", tags=["HealthCheck"])
async def pong():
    return {"ping": "pong!"}
