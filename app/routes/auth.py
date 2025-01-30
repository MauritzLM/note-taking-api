# auth route
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.routes.deps import db_dependency
from app.models.user import User
from app.core.security import get_password_hash

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
    # create user with hashed password
    current_user = User()
    current_user.email = user_create.email
    current_user.password = get_password_hash(user_create.password)
    current_user.username = user_create.username

    session.add(current_user)
    session.commit()
    session.refresh(current_user)

    return {"details": f'user: {current_user}'}



# login
@router.post('/login')
async def login_user():
    ...


# logout
@router.post('/logout')
async def logout_user():
    ...