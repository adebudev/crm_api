from fastapi import FastAPI

app = FastAPI(title="CRM API", version="0.0.1", description="API to crm app")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping", tags=["HealthCheck"])
async def pong():
    return {"ping": "pong!"}
