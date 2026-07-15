from managers.bookManager import BookManager

class TestBookManager:
    """
    Purpose:
        Tests Bible book management.

    Responsibilities:
        - Verify Canonical book lookup.
        - Verify Case-insensitive lookup.
        - Verify alias lookup.
        - Verify invalid book handling.
        - Verify references.
        - Verify invalid chapters.
        - Verify invalid book references
        - Verify createReference() method.
        - Verify createReference() returns None for invalid references.


    Methods:
        - testCanonicalLookup()
        - testCaseInsensitiveLookup()
        - testAliasLookup()
        - testInvalidBookHandling()
        - testReferences()
        - testInvalidChapters()
        - testInvalidBookReferences()
        - testCreateReference()
        - testCreateReferenceInvalid()
    """

    def testCanonicalLookup(self):
        """
        Tests canonical book lookup.

        Parameters: None

        Returns: None

        Verifies:
            'Exodus 2' returns Exodus chapter 2.
        """

        manager = BookManager()
        book = manager.getBook("Exodus")

        assert book is not None
        assert book.name == "Exodus"

    def testCaseInsensitiveLookup(self):
        """
        Tests case-insensitive book lookup.

        Parameters: None

        Returns: None

        Verifies:
            'exodus 2' returns Exodus chapter 2.
        """

        manager = BookManager()
        book = manager.getBook("exodus")

        assert book is not None
        assert book.name == "Exodus"

    def testAliasLookup(self):
        """
        Tests alias book lookup.

        Parameters: None

        Returns: None

        Verifies:
            'Song of Solomon 1' returns Song of Solomon chapter 1.
        """

        manager = BookManager()
        book = manager.getBook("Song of Solomon")

        assert book is not None
        assert book.name == "Song of Solomon"

    def testInvalidBookHandling(self):
        """
        Tests invalid book handling.

        Parameters: None

        Returns: None

        Verifies:
            'InvalidBook 1' returns None.
        """

        manager = BookManager()
        book = manager.getBook("InvalidBook")

        assert book is None

    def testReferences(self):
        """
        Tests valid references.

        Parameters: None

        Returns: None

        Verifies:
            'Exodus 2' returns Exodus chapter 2.
            'Song of Solomon 1' returns Song of Solomon chapter 1.
        """

        manager = BookManager()

        assert manager.isValidReference("Exodus", 2) is True
        assert manager.isValidReference("Song of Solomon", 1) is True

    def testInvalidChapters(self):
        """
        Tests invalid chapters.

        Parameters: None

        Returns: None

        Verifies:
            'Exodus 0' returns False.
            'Song of Solomon 9' returns False.
        """

        manager = BookManager()

        assert manager.isValidReference("Exodus", 0) is False
        assert manager.isValidReference("Song of Solomon", 9) is False

    def testInvalidBookReferences(self):
        """
        Tests invalid book references.

        Parameters: None

        Returns: None

        Verifies:
            'InvalidBook 1' returns False.
            'Exodus 100' returns False.
        """

        manager = BookManager()

        assert manager.isValidReference("InvalidBook", 1) is False
        assert manager.isValidReference("Exodus", 100) is False

    def testCreateReference(self):
        """
        Tests createReference() method.

        Parameters: None

        Returns: None

        Verifies:
            'Exodus 2' returns a valid BibleReference object.
            'Song of Solomon 1' returns a valid BibleReference object.
        """

        manager = BookManager()

        reference1 = manager.createReference("Exodus", 2)
        reference2 = manager.createReference("Song of Solomon", 1)

        assert reference1 is not None
        assert reference1.book.name == "Exodus"
        assert reference1.chapterNumber == 2

        assert reference2 is not None
        assert reference2.book.name == "Song of Solomon"
        assert reference2.chapterNumber == 1

    def testCreateReferenceInvalid(self):
        """
        Tests createReference() method with invalid references.

        Parameters: None

        Returns: None

        Verifies:
            'InvalidBook 1' returns None.
            'Exodus 100' returns None.
        """

        manager = BookManager()

        reference1 = manager.createReference("InvalidBook", 1)
        reference2 = manager.createReference("Exodus", 100)

        assert reference1 is None
        assert reference2 is None