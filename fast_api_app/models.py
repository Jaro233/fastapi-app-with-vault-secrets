from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    genre: str = None
    status: str
    user_rating: int = None
