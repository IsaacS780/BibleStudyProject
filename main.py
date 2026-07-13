from managers.bookManager import BookManager
from managers.studyService import StudyService
from managers.referenceParser import ReferenceParser

# Book - Represents one Bible book
# Bible Catalog -manages a collection of books. Can contain multiple canons and book collections.
# BookManager - Coordinates loading and access of books

#---------------------------------------------------------------------
# MAIN PROGRAM FLOW---------------------------------------------------
#---------------------------------------------------------------------

# Get user input for a Bible reference and parse it into a book name and chapter number.
parser = ReferenceParser()

while True:
    try:
        reference = input("Enter Bible reference: ")
        bookName, chapterNumber = parser.parse(reference)
        break
    except ValueError:
        print("Invalid reference format. Please enter a valid Bible reference (e.g., 'John 3').")

# Get summary from the user.
summary = input("Enter Summary: ")

# Create the BookManager.
bookManager = BookManager()

book = bookManager.getValidBook(bookName, chapterNumber)

# Error condition if reference is invalid.
if book is None:
    print(f"'{bookName} {chapterNumber}' is not a valid Bible reference.")
    exit()

studyService = StudyService()

loadedChapter = studyService.createStudy(book, chapterNumber, summary)

print("\nData loaded fromJSON:")
print(loadedChapter)