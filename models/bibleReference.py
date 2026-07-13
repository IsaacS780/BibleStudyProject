"""
bibleReference.py

Purpose:
    Represents a structured Bible reference.

Primary Class:
    BibleReference
"""

class BibleReference:
    """
    Purpose:
        Represents a location within the Bible.

    Current Responsibilities:
        - Store a Bible book and chapter reference.

    Future Responsibilities:
        - Store verse ranges.
        - Store translations.
        - Support cross references.
        - Connect to study data.

    Methods:
        - toDictionary()
    """

    def __init__(self, book, chapter):
        """
        Creates a Bible reference.

        Parameters:
            book (Book): The validated Bible book.
            chapterNumber (int): The chapter number.

        Returns:
            None
        """

        self.book = book
        self.chapter = chapter

    def toDictionary(self):
        """
        Converts the Bible reference into dictionary format.

        Parameters:
            None

        Returns:
            dict: Bible reference data.
        """

        return {
            "book": self.book.name,
            "chapter": self.chapter
        }