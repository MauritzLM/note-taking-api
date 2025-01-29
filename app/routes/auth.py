# auth route
from fastapi import APIRouter

router = APIRouter(prefix='/users')

# user create
@router.post('/')
async def create_user():
    ...


# login
@router.post('/login')
async def login_user():
    ...


# logout
@router.post('/logout')
async def logout_user():
    ...