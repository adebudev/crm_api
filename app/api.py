from fastapi import FastAPI
from app.common.controllers import user, client
from app.auth.controllers import auth
from app.quotes.controllers import quote_api
from app.invoices.controllers import invoice
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CRM API", version="0.0.1", description="API to crm app")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(quote_api.router)
app.include_router(client.router)
app.include_router(invoice.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping", tags=["HealthCheck"])
async def pong():
    return {"ping": "pong!"}
