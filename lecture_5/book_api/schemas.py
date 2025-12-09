from pydantic import BaseModel, Field
from typing import Optional

# Base schema for Book
class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Book title")
    author: str = Field(..., min_length=1, max_length=100, description="Book author")
    year: Optional[int] = Field(None, ge=1000, le=2100, description="Publication year")

# Schema for creating a new book
class BookCreate(BookBase):
    pass

# Schema for updating a book
class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Book title")
    author: Optional[str] = Field(None, min_length=1, max_length=100, description="Book author")
    year: Optional[int] = Field(None, ge=1000, le=2100, description="Publication year")

# Schema for book response
class BookResponse(BookBase):
    id: int
    
    class Config:
        from_attributes = True  # Allows ORM mode (formerly orm_mode)