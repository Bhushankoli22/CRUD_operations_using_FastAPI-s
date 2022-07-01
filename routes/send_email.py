from fastapi_mail import FastMail, MessageSchema, ConnectionConfig


conf = ConnectionConfig(
    MAIL_USERNAME="Bhushan Koli",
    MAIL_PASSWORD="bhushan.22.",
    MAIL_FROM="bhushannkoli26@gmail.com",
    MAIL_PORT=3000,
    MAIL_SERVER="gsmtp@gmail.com",
    MAIL_FROM_NAME="BHUSHAN",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER='routes/templates/email'
)


async def send_email_async(subject: str, email_to: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype='html',
    )

    fm = FastMail(conf)

    await fm.send_message(message, template_name='email.html')
