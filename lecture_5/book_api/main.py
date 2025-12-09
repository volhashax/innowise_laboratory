from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas
from database import engine, get_db
import uvicorn

# Create FastAPI app
app = FastAPI(
    title="Book Management API",
    description="API for managing books with SQLAlchemy and SQLite",
    version="1.0.0"
)

# Create tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to Book Management API",
        "docs": "/docs",
        "endpoints": {
            "GET /books": "Get all books",
            "GET /books/{id}": "Get a specific book",
            "POST /books": "Create a new book",
            "PUT /books/{id}": "Update a book",
            "DELETE /books/{id}": "Delete a book"
        }
    }

@app.get("/books", response_model=List[schemas.BookResponse])
def get_all_books(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    author: Optional[str] = None,
    year: Optional[int] = None
):
    """Get all books with optional filters"""
    query = db.query(models.Book)
    
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    
    if year:
        query = query.filter(models.Book.year == year)
    
    books = query.offset(skip).limit(limit).all()
    return books

@app.get("/books/search/", response_model=List[schemas.BookResponse])
def search_books(
    db: Session = Depends(get_db),
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    skip: int = 0,
    limit: int = 100
):
    """
    Search books by title, author, or year.
    
    Parameters:
    - title: Search for books containing this text in title (case-insensitive)
    - author: Search for books containing this text in author name (case-insensitive)
    - year: Search for books published in specific year
    - skip: Number of records to skip (for pagination)
    - limit: Maximum number of records to return
    
    Returns:
    - List of books matching the search criteria
    """
    query = db.query(models.Book)
    
    # Apply filters if provided
    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    
    if year:
        query = query.filter(models.Book.year == year)
    
    # Apply pagination
    books = query.offset(skip).limit(limit).all()
    
    return books

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Get a specific book by ID"""
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )
    
    return book

@app.post("/books", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book_data: schemas.BookCreate, db: Session = Depends(get_db)):
    """Create a new book"""
    # Check if book already exists
    existing_book = db.query(models.Book).filter(
        models.Book.title == book_data.title,
        models.Book.author == book_data.author
    ).first()
    
    if existing_book:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book with this title and author already exists"
        )
    
    # Create new book
    new_book = models.Book(
        title=book_data.title,
        author=book_data.author,
        year=book_data.year
    )
    
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return new_book

@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book_data: schemas.BookUpdate, db: Session = Depends(get_db)):
    """Update an existing book"""
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )
    
    # Update fields if provided
    if book_data.title is not None:
        book.title = book_data.title
    
    if book_data.author is not None:
        book.author = book_data.author
    
    if book_data.year is not None:
        book.year = book_data.year
    
    db.commit()
    db.refresh(book)
    
    return book

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book"""
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )
    
    db.delete(book)
    db.commit()
    
    return None

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)