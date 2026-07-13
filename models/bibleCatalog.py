"""
bibleCatalog.py

Purpose:
    Manages the collection of Bible books and provides book lookup.

Primary Class:
    BibleCatalog
"""

class BibleCatalog:
    """
    Purpose:
        Stores and searches the collection of Bible Book objects.

    Current Responsibilities:
        - Retrieve books by name.
        - Normalize user input.
        - Search official names and aliases.

    Future Responsibilities:
        - Filter books by canon.
        - Search books by category.
        - Support multiple Bible collections.

    Methods:
        - normalizeBookName(bookName)
        - getBook(bookName)
        - hasBook(bookName)
    """

    def __init__(self, books):
        self.books = books

    def normalizeBookName(self, bookName):
        """
        Normalizes a book name for comparison.

        Parameters:
            bookName (str): User-entered or stored book name.

        Returns:
            str: Lowercase book name without spaces.

        Workflow:
            1. Convert text to lowercase.
            2. Remove spaces.
            3. Return normalized value.
        """
        return bookName.lower().replace(" ", "")

    def getBook(self, bookName):
        """
        Finds a Bible book using its official name or alias.

        Parameters:
            bookName (str): User-entered Bible book name.

        Returns:
            Book: Matching Book object, or None if not found.

        Workflow:
            1. Normalize user input.
            2. Search official book names.
            3. Search book aliases.
            4. Return matching Book object.
        """
        # Make user input bookName lower case so input is not case sensitive.
        normalizedBookName = self.normalizeBookName(bookName)

        # Loop through dictionary key for books and search for a match with keys name/book. Return the book if found.
        for name, book in self.books.items():
            if self.normalizeBookName(name) == normalizedBookName:
                return book
            # Search aliases for a match.
            for alias in book.aliases:
                if self.normalizeBookName(alias) == normalizedBookName:
                    return book       
        # If above has no values, book does not exist.
        return None
    
    def hasBook(self, bookName):
        """
        Checks whether a Bible book exists.

        Parameters:
            bookName (str): Book name or alias to search for.

        Returns:
            bool: True if found; otherwise False.
        """
        return self.getBook(bookName) is not None