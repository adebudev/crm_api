from fastapi import status, APIRouter
from fastapi_mail import FastMail, MessageSchema
from fastapi import Response
from starlette.responses import JSONResponse

from app.config.email_config import conf

router = APIRouter(prefix="/send-email")

async def send_email_async(subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        template_body=body
    )

    fm = FastMail(conf)
    await fm.send_message(message, template_name='email.html')

@router.get('/')
async def send_email_asynchronous(response: Response):
    email = "delaasuncionbuelvasadrian@gmail.com"
    await send_email_async('Recuperar contraseña', email,
    {
        "title": "PERSONAL CRM",
        "user_email": email
    })
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return response