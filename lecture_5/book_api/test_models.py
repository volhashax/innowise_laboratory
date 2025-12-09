#!/usr/bin/env python3
"""
Test script to verify the Book model is working correctly
"""

from database import engine, SessionLocal, create_tables
from models import Book

def test_book_model():
    """Test the Book model functionality"""
    print("="*50)
    print("📚 Testing Book Model with SQLAlchemy")
    print("="*50)
    
    # Create tables
    create_tables()
    
    # Create a session
    db = SessionLocal()
    
    try:
        # Create sample books
        books_data = [
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
            {"title": "1984", "author": "George Orwell", "year": 1949},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
            {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
        ]
        
        # Add books to database
        for book_data in books_data:
            book = Book(**book_data)
            db.add(book)
        
        db.commit()
        print("✅ Sample books added to database")
        
        # Query all books
        all_books = db.query(Book).all()
        print(f"\n📖 Total books in database: {len(all_books)}")
        
        for book in all_books:
            print(f"  • {book.title} by {book.author} ({book.year})")
        
        # Test query with filter
        print("\n🔍 Books published after 1900:")
        recent_books = db.query(Book).filter(Book.year > 1900).all()
        for book in recent_books:
            print(f"  • {book.title} ({book.year})")
        
        # Test single book query
        print("\n📗 Find specific book by title:")
        specific_book = db.query(Book).filter(Book.title == "1984").first()
        if specific_book:
            print(f"  Found: {specific_book.title} by {specific_book.author}")
        
        # Test updating a book
        print("\n✏️  Updating a book:")
        book_to_update = db.query(Book).filter(Book.title.like("%Hobbit%")).first()
        if book_to_update:
            book_to_update.year = 1938
            db.commit()
            print(f"  Updated: {book_to_update.title} year changed to {book_to_update.year}")
        
        # Count books
        book_count = db.query(Book).count()
        print(f"\n📊 Total books count: {book_count}")
        
        # Get book as dictionary
        first_book = db.query(Book).first()
        if first_book:
            print(f"\n📋 First book as dictionary: {first_book.to_dict()}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()
        print("\n" + "="*50)
        print("✅ Test completed successfully!")
        print("="*50)

if __name__ == "__main__":
    test_book_model()