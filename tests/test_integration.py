# tests/test_integration.py
from fastapi.testclient import TestClient

from fast_api_app.app import app

client = TestClient(app)


def test_read_books_integration():
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()["books"]
    # Here you could check for some expected properties of the books, e.g.:
    for book in books:
        assert "title" in book
        assert "author" in book
        # etc.


def test_add_book_integration():
    new_book_data = {
        "title": "Integration Test Book",
        "author": "Integration Test Author",
        "genre": "Integration Test Genre",
        "status": "to read",
        "user_rating": 5,
    }

    response = client.post("/books", json=new_book_data)
    assert (
        response.status_code == 201
    )  # or check for the actual status code your API should return
    # You can also check the content of the response if needed
