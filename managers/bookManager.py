import json
from models.book import Book

class BookManager:

    def __init__(self):
        self.books = self.createBooks()

    # Use Bible/books.json to store data. Method reads file and loods books into Python dictionary.
    def createBooks(self):
        with open("Bible/books.json", "r") as file:
            bookData = json.load(file)

        books = {}

        for name, data in bookData.items():
            books[name] = Book(name, data["chapters"], data["canon"])

        return books
    
    def getBook(self, bookName):
        return self.books.get(bookName)