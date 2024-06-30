from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
import crud

models.Base.metadata.create_all(bind=engine)
db: Session = SessionLocal()

print("Creating a new book")
new_book = crud.create_book(
    db,
    title="Test book",
    author="Test author",
    price=99.99,
    publication_date="2023-10-10",
)
print(f"Created book: {new_book}")

print("\nRetrieving the book")
retrieved_book = crud.get_book(db, book_id=new_book.id)
print(f"Retrieved book with id: {retrieved_book}")

print("\nGetting multiple books")
books = crud.get_books(db)
print(f"Books: {books}")

print("\nUpdating the book's title and price")
updated_book_1 = crud.update_book(
    db, book_id=new_book.id, title="Modified book", price=12.99
)
print(f"Updated book: {updated_book_1.title, updated_book_1.price}")

print("\nUpdating the book's author and publication date")
updated_book_2 = crud.update_book(
    db, book_id=new_book.id, author="Modified author", publication_date="2024-10-10"
)
print(f"Updated book: {updated_book_2.author, updated_book_2.publication_date}")

print("\nDeleting the book...")
deleted_book = crud.delete_book(db, book_id=new_book.id)
print(f"Deleted book: {deleted_book}")

db.close()
