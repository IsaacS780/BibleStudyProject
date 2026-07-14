"""
book.py

Purpose:
    Represents a single Bible book.

Primary Class:
    Book
"""

class Book:
    """
    Purpose:
        Represents one Bible book and its metadata.

    Current Responsibilities:
        - Store book information.
        - Validate chapter numbers.

    Future Responsibilities:
        - Store testament information.
        - Store categories.
        - Store alternate names.

    Methods:
        - isValidChapter(chapterNumber)
    """
    
    def __init__(self, name, chapters, canon, testament, aliases=None):
        """
        Creates a Book object.

        Parameters:
            name (str): Official book name.
            chapters (int): Number of chapters.
            canon (str): Canon this book belongs to.
            testament (str): Old or New Testament.
            aliases (list): Alternate book names.

        Returns:
            None

        Workflow:
            1. Store the book information.
            2. Store aliases, or an empty list if none exist.
        """
        self.name = name
        self.chapters = chapters
        self.canon = canon
        self.testament = testament
        self.aliases = aliases or []

    # Checks whether a requested chapter exists for this specific book.
    def isValidChapter(self, chapterNumber):
        """
        Determines whether a chapter exists.

        Parameters:
            chapterNumber (int): Chapter to validate.

        Returns:
            bool: True if valid; otherwise False.
        """
        return 1 <= chapterNumber <= self.chapters
    
    def isOldTestament(self):
        """
        Determines whether this book belongs to the Old Testament.

        Parameters: None

        Returns:
            bool: True if the book is in the Old Testament.
        """

        return self.testament == "Old"

    def isNewTestament(self):
        """
        Determines whether this book belongs to the New Testament.

        Parameters: None

        Returns:
            bool: True if the book is in the New Testament.
        """

        return self.testament == "New"