from fastapi import APIRouter, Request, Form, File, UploadFile
from typing import Annotated

router = APIRouter(prefix='/notes')

# dependencies -> auth, db

# read note
@router.post('/')
async def get_note():
    ...

# create note
@router.post('/create')
async def create_note():
    ...


# update note
@router.put('/update')
async def update_note():
    ...

# archive note
@router.put('/archive')
async def archive_note():
    ...


# delete note
@router.delete('/delete')
async def delete_note():
    ...
