class BibleCatalog:
    # Can later add methods like: catalog.getBooksByCanon("Protestant")
    # catalog.getBooksByCanon("Protestant")

    def __init__(self, books):
        self.books = books

    def getBook(self, bookName):
        return self.books.get(bookName)