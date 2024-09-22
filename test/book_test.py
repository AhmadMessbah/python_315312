from model.entity.book import Book

book = Book("Python Book", "python", 100)
print(book)
print(book.to_tuple())