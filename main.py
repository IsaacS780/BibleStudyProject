from managers.studyService import StudyService
from managers.referenceParser import ReferenceParser
from managers.bookManager import BookManager


# Book - Represents one Bible book.
# BibleCatalog - Manages a collection of books. Can contain multiple canons and book collections.
# BookManager - Coordinates loading and access of books.

# ---------------------------------------------------------------------
# MAIN PROGRAM FLOW
# ---------------------------------------------------------------------

# Create managers used throughout the application.
parser = ReferenceParser()
bookManager = BookManager()

# Get user input for a Bible reference and validate it.
while True:
    try:
        reference = input("Enter Bible reference: ")

        bookName, chapterNumber = parser.parse(reference)

        bibleReference = bookManager.createReference(bookName, chapterNumber)

        if bibleReference is None:
            print(f"'{bookName} {chapterNumber}' is not a valid Bible reference.")
            continue

        break

    except ValueError:
        print("Invalid reference format. Please enter a valid Bible reference (e.g., 'John 3').")


# Get summary from the user.
summary = input("Enter Summary: ")

# Retrieve the validated Book object from the BibleReference.
book = bibleReference.book

# Create the study.
studyService = StudyService()

loadedChapter = studyService.createStudy(book, chapterNumber, summary)

print("\nData loaded from JSON:")
print(loadedChapter)