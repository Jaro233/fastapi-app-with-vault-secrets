from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


# Route to serve the index.html
@router.get("/", response_class=HTMLResponse)
async def read_index():
    return Path("static/html/index.html").read_text()


# Route to serve the add_book.html
@router.get("/add-book", response_class=HTMLResponse)
async def add_book():
    return Path("static/html/add_book.html").read_text()


# Route to serve the view_edit_book.html
@router.get("/edit-book", response_class=HTMLResponse)
async def edit_book():
    return Path("static/html/view_edit_book.html").read_text()
