from sqlalchemy.orm import Session
from models import Book
from typing import Optional

# Create, Retrieve, Update, Delete


# C
def create_book(
    db: Session, title: str, author: str, price: float, publication_date: str
):
    db_book = Book(
        title=title, author=author, price=price, publication_date=publication_date
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# R
def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()


# U
def update_book(
    db: Session,
    book_id: int,
    title: Optional[str] = None,
    author: Optional[str] = None,
    price: Optional[float] = None,
    publication_date: Optional[str] = None,
):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        if title is not None:
            db_book.title = title
        if author is not None:
            db_book.author = author
        if price is not None:
            db_book.title = price
        if publication_date is not None:
            db_book.publication_date = publication_date
        db.commit()
        db.refresh(db_book)
    return db_book


# D
def delete_book(db: Session, book_id):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
