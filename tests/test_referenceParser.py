from managers.referenceParser import ReferenceParser

class TestReferenceParser:
    """
    Purpose:
        Tests Bible reference parsing and normalization.

    Responsibilities:
        - Verify valid reference formats.
        - Verify input normalization.
        - Verify invalid input handling.

    Methods:
        - testStandardReference()
        - testLowercaseReference()
        - testNumberedBookWithSpace()
        - testNumberedBookWithoutSpace()
        - testAliasReference()
        - testInvalidReference()
    """

    def testStandardReference(self):
        """
        Tests a standard Bible reference.

        Parameters:
            None

        Returns:
            None

        Verifies:
            'Exodus 2' returns Exodus chapter 2.
        """

        parser = ReferenceParser()
        bookName, chapterNumber = parser.parse("Exodus 2")

        assert bookName == "Exodus"
        assert chapterNumber == 2

    def testLowercaseReference(self):
        """
        Tests lowercase input normalization.

        Parameters:
            None

        Returns:
            None

        Verifies:
            'exodus 2' is accepted.
        """

        parser = ReferenceParser()
        bookName, chapterNumber = parser.parse("exodus 2")

        assert bookName == "Exodus"
        assert chapterNumber == 2

    def testNumberedBookWithSpace(self):
        """
        Tests numbered Bible books with spacing.

        Parameters:
            None

        Returns:
            None

        Verifies:
            '1 chronicles 1' is normalized correctly.
        """

        parser = ReferenceParser()

        bookName, chapterNumber = parser.parse("1 chronicles 1")

        assert bookName == "1 Chronicles"
        assert chapterNumber == 1


    def testNumberedBookWithoutSpace(self):
        """
        Tests numbered Bible books without spacing.

        Parameters:
            None

        Returns:
            None

        Verifies:
            '1chronicles 1' is normalized correctly.
        """

        parser = ReferenceParser()

        bookName, chapterNumber = parser.parse("1chronicles 1")

        assert bookName == "1Chronicles"
        assert chapterNumber == 1

    def testInvalidReference(self):
        """
        Tests invalid Bible reference handling.

        Parameters:
            None

        Returns:
            None

        Verifies:
            Invalid references raise ValueError.
        """

        parser = ReferenceParser()

        try:
            parser.parse("Exodus")

            assert False

        except ValueError:
            assert True