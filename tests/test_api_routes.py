# tests/test_api_routes.py
from fastapi.testclient import TestClient

from fast_api_app.app import app

client = TestClient(app)


def test_read_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), object)  # assuming the endpoint returns a list


def test_add_book():
    new_book_data = {
        "title": "New Book",
        "author": "Author Name",
        "genre": "Fiction",
        "status": "to read",
        "user_rating": 5,
    }

    response = client.post("/books", json=new_book_data)
    assert (
        response.status_code == 201
    )  # Assuming 201 is the success status code for creation
    # Further assertions can be added to check the response content


def test_add_book_invalid_data():
    invalid_book_data = {
        "title": "New Book",
        "author": "Author Name",
        "genre": "InvalidGenre",  # Provide a valid string here
        "status": "",
        "user_rating": "",  # Provide an intentionally incorrect value (like a string)
    }

    response = client.post("/books", json=invalid_book_data)
    assert (
        response.status_code == 422
    )  # Assuming invalid data is handled with a 400 status


def test_update_book():
    update_data = {
        "title": "Updated Book",
        "author": "Updated Author Name",
        "genre": "Non-Fiction",
        "status": "reading",
        "user_rating": 4,
    }

    # Assuming there's a book with ID 1 in the test database
    response = client.put("/books/1", json=update_data)
    assert (
        response.status_code == 200
    )  # Assuming 200 is the success status code for update
    # Further assertions can be added to check the response content


def test_delete_book():
    # Assuming there's a book with ID 1 in the test database
    response = client.delete("/books/1")
    assert (
        response.status_code == 200
    )  # Assuming 200 is the success status code for deletion
    # Further assertions can be added to check the response content
