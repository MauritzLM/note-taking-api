from fastapi import APIRouter, Request, Form, File, UploadFile, Depends
from typing import Annotated
from pydantic import BaseModel, UUID4
from app.models.user import User
from app.models.note import Note
from app.core.security import get_current_user
from app.routes.deps import db_dependency
import datetime

router = APIRouter(prefix='/notes')

# dependencies -> auth, db
# rate limiter*

class NoteCreate(BaseModel):
    title: str
    text: str
    tags: list[str]

class PublicNote(BaseModel):
    id: UUID4
    title: str
    text: str
    isArchived: bool
    tags: list[str]
 
class NoteId(BaseModel):
    id: UUID4


# read note
@router.post('/')
async def get_note():
    ...

# create note
@router.post('/create')
async def create_note(session: db_dependency, note: NoteCreate, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        new_note = Note()
        new_note.author = current_user.id
        new_note.title = note.title
        new_note.text = note.text
        new_note.tags = note.tags.copy()
    
        session.add(new_note)
        session.commit()
        session.refresh(new_note)
    
    except:
        return {"details": "An error occured"}

    return {"details": "Note created"}


# update note
@router.put('/update')
async def update_note(session: db_dependency, current_note: PublicNote, current_user: Annotated[User, Depends(get_current_user)]):
    # check if any changes?*
    try:
        session.query(Note).filter(Note.id == current_note.id).update({ Note.isArchived: current_note.isArchived, Note.tags: current_note.tags.copy(), Note.text: current_note.text, Note.title: current_note.title, Note.date: datetime.datetime.now() })
        session.commit()
    
    except:
        return {"details": "An error occured"}

    return {"details": "Note updated"}

# archive note
@router.put('/archive')
async def archive_note(session: db_dependency, current_note: NoteId, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        session.query(Note).filter(Note.id == current_note.id).update({ Note.isArchived: True })
        session.commit()

    except:
        return {"details": "An error occured"}    
    
    return {"details": "note archived"}

# restore note
@router.put('/restore')
async def archive_note(session: db_dependency, current_note: NoteId, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        session.query(Note).filter(Note.id == current_note.id).update({ Note.isArchived: False })
        session.commit()

    except:
        return { "details": "An error occured" }    
    
    return { "details": "note restored" }


# get all notes
@router.get('/all', response_model=list[PublicNote])
async def get_all_notes(session: db_dependency, current_user: Annotated[User, Depends(get_current_user)]):
    all_notes = session.query(Note).filter(Note.author == current_user.id).all()

    return all_notes


# delete note
@router.post('/delete')
async def delete_note(session: db_dependency, current_note: NoteId, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        session.query(Note).filter(Note.id == current_note.id).delete()
        session.commit()

    except:
        return {"details": "An error occured"}    
    
    return {"details": "note deleted"}
