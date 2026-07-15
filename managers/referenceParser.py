from models.bibleReference import BibleReference

"""
referenceParser.py

Purpose:
    Parses user-entered Bible references into structured data.

Primary Class:
    ReferenceParser
"""


class ReferenceParser:
    """
    Purpose:
        Converts a Bible reference entered by the user into
        a normalized book name and chapter number.

    Current Responsibilities:
        - Parse a complete Bible reference.
        - Separate the book name from the chapter number.
        - Normalize book formatting.

    Future Responsibilities:
        - Parse verse references.
        - Support chapter ranges.

    Methods:
        - parse(reference)
        - normalizeBookName(bookName)
    """

    def parse(self, reference):
        """
        Parses a Bible reference.

        Parameters:
            reference (str): A Bible reference such as "John 3".

        Returns:
            tuple: (bookName, chapterNumber)

        Workflow:
            1. Remove leading/trailing whitespace.
            2. Split reference into parts.
            3. Validate chapter number.
            4. Extract book name.
            5. Normalize book formatting.
            6. Return parsed values.
        """

        reference = reference.strip()

        if not reference:
            raise ValueError("Reference cannot be empty.")
        
        parts = reference.split()

        if len(parts) < 2:
            raise ValueError("Reference must contain a book name and chapter number.")

        if not parts[-1].isdigit():
            raise ValueError("Last part of reference must be a chapter number.")

        bookName = " ".join(parts[:-1])
        chapterNumber = int(parts[-1])

        return self.normalizeBookName(bookName), chapterNumber
    
    def normalizeBookName(self, bookName):
        """
        Normalizes Bible book formatting.

        Parameters:
            bookName (str): The user-entered Bible book name.

        Returns:
            str: The normalized book name.

        Workflow:
            1. Remove extra spaces.
            2. Convert book words to title case.
            3. Preserve numeric prefixes.
        """

        bookName = " ".join(bookName.split())

        return bookName.title()