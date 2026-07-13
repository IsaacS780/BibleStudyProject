class BibleCatalog:
    # Can later add methods like: catalog.getBooksByCanon("Protestant")
    # catalog.getBooksByCanon("Protestant")

    def __init__(self, books):
        self.books = books

    # Return book data for bookName in catalog.
    def getBook(self, bookName):
        return self.books.get(bookName)
    
    # Check if bookName is in catalog and return True/False.
    def hasBook(self, bookName):
        return bookName in self.books