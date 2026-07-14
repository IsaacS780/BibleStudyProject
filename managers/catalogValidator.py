"""
catalogValidator.py

Purpose:
    Validates the structure of the Bible catalog before Book objects are created.

Primary Class:
    CatalogValidator
"""

class CatalogValidator:
    """
    Purpose:
        Validates each book entry in the Bible catalog.

    Current Responsibilities:
        - Verify required fields exist.
        - Raise descriptive errors when data is invalid.

    Future Responsibilities:
        - Validate data types.
        - Validate chapter counts.
        - Validate duplicate aliases.
        - Validate canonical ordering.

    Methods:
        - validate(bookData)
    """

    REQUIRED_FIELDS = ["chapters", "canon", "testament", "aliases"]

    def validate(self, bookData):
        """
        Validates every book in the catalog.

        Parameters:
            bookData (dict): Dictionary loaded from books.json.

        Returns:
            None

        Workflow:
            1. Loop through each book.
            2. Check each required field.
            3. Raise a descriptive error if any field is missing.
        """

        for bookName, data in bookData.items():

            for field in self.REQUIRED_FIELDS:
                if field not in data:
                    raise ValueError(f"Missing required field '{field}' for book '{bookName}'")