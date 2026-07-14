"""
bibleReference.py

Purpose:
    Represents a validated location within the Bible.

Primary Class:
    BibleReference
"""


class BibleReference:
    """
    Purpose:
        Represents a validated Bible book and chapter reference.

    Current Responsibilities:
        - Store a validated Bible book.
        - Store a chapter number.

    Future Responsibilities:
        - Store verse ranges.
        - Store translations.
        - Store cross references.
        - Connect to study generation.

    Methods:
        - toDictionary()
    """

    def __init__(self, book, chapterNumber):
        """
        Creates a Bible reference.

        Parameters:
            book (Book): Validated Bible book object.
            chapterNumber (int): Validated chapter number.

        Returns:
            None
        """

        self.book = book
        self.chapterNumber = chapterNumber

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
            "chapter": self.chapterNumber
        }