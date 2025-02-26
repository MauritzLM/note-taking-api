# jwt, password hash
import jwt
from passlib.context import CryptContext
import bcrypt
from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel
from app.routes.deps import db_dependency
from app.models.user import User

import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
load_dotenv(env_path)

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# url?*
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(
       plain_password.encode('utf8'),
       hashed_password.encode('utf8')
    )

def get_password_hash(password):
    return bcrypt.hashpw(
        password.encode('utf8'),
        bcrypt.gensalt(),
    )

# create access token function
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# authorize function
async def get_current_user(session: db_dependency, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    
    current_user = session.query(User).filter(User.username == token_data.username).first()
    if current_user is None:
        raise credentials_exception
    return current_user