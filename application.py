"""
application.py

Purpose:
    Coordinates the overall Bible Study Agent workflow.

Primary Class:
    Application
"""

from email import parser

from managers import bookManager
from managers.bookManager import BookManager
from managers.referenceParser import ReferenceParser
from managers.studyService import StudyService


class Application:
    """
    Purpose:
        Coordinates the Bible Study Agent application.

    Current Responsibilities:
        - Gather user input.
        - Validate Bible references.
        - Coordinate study creation.

    Future Responsibilities:
        - Generate AI studies.
        - Coordinate Obsidian integration.
        - Update knowledge databases.
        - Execute LangGraph workflows.

    Methods:
        - run()
        - getBibleReference()
    """

    def __init__(self):
        """
        Creates the application and initializes its services.

        Parameters: None

        Returns: None
        """
        self.parser = ReferenceParser()
        self.bookManager = BookManager()
        self.studyService = StudyService()

    def getBibleReference(self):
        """
        Prompts the user for a Bible reference until a valid reference is entered.

        Parameters: None

        Returns:
            BibleReference: A validated Bible reference.

        Workflow:
            1. Read user input.
            2. Parse the reference.
            3. Validate the reference.
            4. Return the validated BibleReference.
        """

        while True:
            try:
                reference = input("Enter Bible reference: ")

                bookName, chapterNumber = self.parser.parse(reference)

                bibleReference = self.bookManager.createReference(bookName, chapterNumber)

                if bibleReference is None:
                    print(f"'{bookName} {chapterNumber}' is not a valid Bible reference.")
                    continue

                return bibleReference

            except ValueError:
                print("Invalid reference format. Please enter a valid Bible reference (e.g., 'John 3').")

    def run(self):
        """
        Runs the Bible Study Agent.

        Parameters: None

        Returns: None

        Workflow:
            1. Get a validated Bible reference.
            2. Request the chapter summary.
            3. Create the study.
            4. Display the saved study data.
        """

        bibleReference = self.getBibleReference()

        # Get summary from the user.
        summary = input("Enter Summary: ")

        loadedChapter = self.studyService.createStudy(bibleReference.book, bibleReference.chapter, summary)

        print("\nData loaded from JSON:")
        print(loadedChapter)