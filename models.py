from sqlalchemy import Column, Integer, Float, String, Date
from database import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False, index=True)
    price = Column(Float)
    publication_date = Column(Date)
