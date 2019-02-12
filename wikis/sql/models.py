from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    name = Column(String)
    author = Column(String)

    def __repr__(self):
        return f'{self.name} : {self.author}'


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    comment = Column(String)
    quality = Column(String)
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship("Book", back_populates="article")

    def __repr__(self):
        return f'{self.book} - {self.title}'
