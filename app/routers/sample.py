from fastapi import APIRouter

router = APIRouter()

# @router.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse(request=request, name='index.html')

@router.get('/test')
async def read_user_me():
    return {"username": "fakecurrentuser"}
