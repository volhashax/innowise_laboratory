from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    """
    Book model representing a book in the database.
    
    Attributes:
        id (int): Primary key
        title (str): Book title (required)
        author (str): Book author (required)
        year (int): Publication year (optional)
    """
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    author = Column(String(100), nullable=False, index=True)
    year = Column(Integer, nullable=True)
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})>"
    
    def to_dict(self):
        """Convert book object to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year
        }