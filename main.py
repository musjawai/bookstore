from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
import crud
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/books/")
def create_book(
    title: str,
    author: str,
    price: float,
    publication_date: str,
    db: Session = Depends(get_db()),
):
    return crud.create_book(
        db=db,
        title=title,
        author=author,
        price=price,
        publication_date=publication_date,
    )


@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db())):
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.get("/books/")
def read_book(skip: int = 0, limit: int = 10, db: Session = Depends(get_db())):
    books = crud.get_books(db=db, skip=skip, limit=limit)
    return books
