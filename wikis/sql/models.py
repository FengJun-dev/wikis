from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    name = Column(String)
    author = Column(String)

    def __repr__(self):
        pass


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    comment = Column(String)
    quality = Column(String)

    def __repr__(self):
        pass
