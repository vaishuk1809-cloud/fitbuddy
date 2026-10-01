from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@router.get("/users")
async def all_users(request: Request):
    return templates.TemplateResponse(
        "all_users.html",
        {"request": request}
    )


@router.get("/result")
async def result(request: Request):
    return templates.TemplateResponse(
        "result.html",
        {"request": request}
    )
