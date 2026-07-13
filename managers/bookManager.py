import json

from config import BIBLE_BOOKS_FILE
from models.book import Book
from models.bibleCatalog import BibleCatalog

"""
bookManager.py

Purpose:
    Loads the Bible catalog and provides access to Bible books.

Primary Class:
    BookManager

Dependencies:
    - BibleCatalog
    - Book
    - books.json
"""

class BookManager:

    def __init__(self):
        self.catalog = self.createBooks()

    # Use Bible/books.json to store data. Method reads file and loods books into Python dictionary.
    def createBooks(self):
        with open(BIBLE_BOOKS_FILE, "r") as file:
            bookData = json.load(file)

        books = {}

        for name, data in bookData.items():
            books[name] = Book(name, data["chapters"], data["canon"])

        return BibleCatalog(books)
    
    def getBook(self, bookName):
        # Returns None if no book exists
        return self.catalog.getBook(bookName)
    
    def isValidReference(self, bookName, chapterNumber):
        # Check to ensure book exists in catalog.
        if not self.catalog.hasBook(bookName):
            return False

        # Get book  
        book = self.getBook(bookName)

        # Error if book has no data.
        if book is None:
            return False
        
        # Return True if reference is valid.
        return book.isValidChapter(chapterNumber)
    
    # Validates a Bible reference and returns the corresponding Book object when successful.
    def getValidBook(self, bookName, chapterNumber):
        book = self.getBook(bookName)

        # .get() will return None if it doesn't exist.
        if book is None:
            return None
        
        if not book.isValidChapter(chapterNumber):
            return None
        
        # Reference validated above. Return book object.    
        return book