from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
from fastapi import FastAPI
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List
from routes.send_email import send_email_async
app = FastAPI()
user = APIRouter()

# @user.get("/")
# async def read_something():
#     return {"message":"Hello World"}


@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()


@user.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchone()


@user.get("/{id}")
async def read_data(id: int):
    conn.execute(users.select().where(users.c.id == id))
    return conn.execute(users.select()).fetchone()

# @user.get("/{id}")
# async def read_data(id: int):
#     conn.execute(users.select().where (users.c.id == id))
#     return conn.execute(users.select()).fetchone()


@user.put("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    return conn.execute(users.select()).fetchall()


@user.post("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()


@user.patch("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()


@user.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()


class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_FROM="email",
    MAIL_USERNAME="email",
    MAIL_FROM_NAME="BHUSHAN",
    MAIL_PASSWORD="password",
    MAIL_PORT=8000,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False
)


async def send_email_async(subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype='html',
    )

    fm = FastMail(conf)
    await fm.send_message(message, template_name='email.html')


@user.get('/send_email_async')
def send_email_asynchronous():
    send_email_async('Hello World', 'to_mail',
                     'Hello World')
    return 'Success'
