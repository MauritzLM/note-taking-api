# auth route
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.routes.deps import db_dependency
from app.models.user import User
from app.core.security import get_password_hash, verify_password, create_access_token, Token
from datetime import timedelta

router = APIRouter(prefix='/users')

class UserCreate(BaseModel):
    username: str
    password: str
    email: str


# user create
@router.post('/create')
async def create_user(session: db_dependency, user_create: UserCreate):
    # check if user already in db (by email)
    current_user = session.query(User).filter(User.email == user_create.email).first()
    if current_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists.",
        )
    # sanitize data?*
    # create user with hashed password
    current_user = User()
    current_user.email = user_create.email
    # decode hashed password
    current_user.password = get_password_hash(user_create.password).decode('utf8')
    current_user.username = user_create.username

    session.add(current_user)
    session.commit()
    session.refresh(current_user)

    return {"details": 'user created'}



# login
@router.post('/login')
async def login_user(session: db_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # authenticate user
    current_user = session.query(User).filter(User.username == form_data.username).first()
    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # verify password
    correct_password = verify_password(form_data.password, current_user.password)
    if not correct_password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # create access token
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": current_user.username}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")


# logout
@router.post('/logout')
async def logout_user():
    ...