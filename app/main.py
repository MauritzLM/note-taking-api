from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from app.routes import notes
from app.routes import auth
from typing import Annotated
import app.models.user as users
from app.core.config import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
users.Base.metadata.create_all(bind=engine)

origins = ['http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes.router)
app.include_router(auth.router)