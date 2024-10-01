import re

from sqlalchemy import Column, Integer, String, Boolean

from model.entity.book_validation import *
from model.entity.base import Base


# model.entity
# __init__
# getter/setter
# property
# __repr__, __str__

class Book(Base):
    __tablename__ = "book_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title",String(20), nullable=False)
    _author = Column("author", String(20), nullable=False)
    _pages = Column("pages", Integer, default=0)

    def __init__(self,id, title, author, pages):
        self._id = id
        self.title = title
        self.author = author
        self.pages = pages


    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title_validator(title)

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author_validator(author)

    def get_pages(self):
        return self._pages

    def set_pages(self, pages):
        self._pages = positive_int(pages)

    title = property(get_title, set_title)
    author = property(get_author, set_author)
    pages = property(get_pages, set_pages)


