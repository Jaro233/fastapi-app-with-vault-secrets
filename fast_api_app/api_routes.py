from fastapi import APIRouter, HTTPException

from fast_api_app.db import db_conn
from fast_api_app.models import Book

router = APIRouter()


# List all books
@router.get("/books", status_code=200)
async def read_books():
    cur = db_conn()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()  # Close the cursor after the operation
    return {"books": books}


# Add a new book
@router.post("/books", status_code=201)
async def add_book(book: Book):
    cur = db_conn()
    cur.execute(
        "INSERT INTO books (title, author, genre, status, user_rating) VALUES (%s, %s, %s, %s, %s)",
        (book.title, book.author, book.genre, book.status, book.user_rating),
    )
    cur.connection.commit()  # Commit the transaction
    cur.close()
    return {"message": "Book added successfully"}


# Get a specific book
@router.get("/books/{book_id}")
async def get_book(book_id: int):
    cur = db_conn()
    cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cur.fetchone()
    if book:
        return book
    cur.close()  # Close the cursor after the operation
    raise HTTPException(status_code=404, detail="Book not found")


# Update book information
@router.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    cur = db_conn()
    cur.execute(
        "UPDATE books SET title = %s, author = %s, genre = %s, status = %s, user_rating = %s WHERE id = %s",
        (book.title, book.author, book.genre, book.status, book.user_rating, book_id),
    )
    cur.connection.commit()  # Commit the transaction
    cur.close()
    return {"message": "Book updated successfully"}


# Delete a book
@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    cur = db_conn()
    cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
    cur.connection.commit()  # Commit the transaction
    cur.close()
    return {"message": "Book deleted successfully"}
