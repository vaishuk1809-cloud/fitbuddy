from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="FitBuddy")

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/users")
async def users(request: Request):
    return templates.TemplateResponse(
        "all_users.html",
        {"request": request}
    )


@app.get("/result")
async def result(request: Request):
    return templates.TemplateResponse(
        "result.html",
        {"
