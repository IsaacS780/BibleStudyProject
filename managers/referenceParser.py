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
        Converts a Bible reference entered by the user into a book name and chapter number.

    Current Responsibilities:
        - Parse a complete Bible reference.
        - Separate the book name from the chapter number.

    Future Responsibilities:
        - Parse verse references.
        - Support chapter ranges.
        - Support abbreviations.
        - Support alternate book names.

    Methods:
        - parse(reference)
    """

    def parse(self, reference):
        """
        Parses a Bible reference.

        Parameters:
            reference (str): A Bible reference such as "John 3".

        Returns:
            tuple: (bookName, chapterNumber)

        Workflow:
            1. Remove leading and trailing whitespace.
            2. Split the reference into words.
            3. Verify the reference contains a book and chapter.
            4. Verify the last word is a chapter number.
            5. Join the remaining words into the book name.
            6. Return the parsed values.
        """

        reference = reference.strip()

        if not reference:
            raise ValueError("Reference cannot be empty.")
        
        parts = reference.split()

        if len(parts) < 2:
            raise ValueError("Reference must contain a book name and chapter number.")

        parts = reference.strip().split()

        if not parts[-1].isdigit():
            raise ValueError("Last part of reference must be a chapter number.")

        bookName = " ".join(parts[:-1])
        chapterNumber = int(parts[-1])

        return bookName, chapterNumber