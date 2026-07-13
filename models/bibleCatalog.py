class BibleCatalog:
    # Can later add methods like: catalog.getBooksByCanon("Protestant")
    # catalog.getBooksByCanon("Protestant")
    # Add method to normalize input for book names.

    def __init__(self, books):
        self.books = books

    # Returns a normalized string with all letters in lowercase and all spaces removed.
    def normalizeBookName(self, bookName):
        return bookName.lower().replace(" ", "")

    # Return book data for bookName in catalog.
    def getBook(self, bookName):
        # Make user input bookName lower case so input is not case sensitive.
        normalizedBookName = self.normalizeBookName(bookName)

        # Loop through dictionary key for books and search for a match with keys name/book. Return the book if found.
        for name, book in self.books.items():
            if self.normalizeBookName(name) == normalizedBookName:
                return book
        
        # If above has no values, book does not exist.
        return None
    
    # Check if bookName is in catalog and return True/False.
    def hasBook(self, bookName):
        return self.getBook(bookName) is not None