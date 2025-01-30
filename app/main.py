from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer
from app.routes import notes
from app.routes import auth
from typing import Annotated
import app.models.user as users
from app.core.config import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
users.Base.metadata.create_all(bind=engine)

app.include_router(notes.router)
app.include_router(auth.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}




