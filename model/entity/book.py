import re

from validation import *


# model.entity
# __init__
# getter/setter
# property
# __repr__, __str__

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())

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


book = Book("Python Book", "python", 100)
print(book)
print(book.to_tuple())