from models.chapter import Chapter
from managers.studyNotes import createStudyNote
from managers.dataManager import saveChapterData, loadChapterData
from managers.bookManager import BookManager

# Book - Represents one Bible book
# Bible Catalog -manages a collection of books. Can contain multiple canons and book collections.
# BookManager - Coordinates loading and access of books

#---------------------------------------------------------------------
# MAIN PROGRAM FLOW---------------------------------------------------
#---------------------------------------------------------------------

# Get user input for what to study.
bookName = input("Enter book: ")

# Get chapter number. Must be an integer.
while True:
    try:
        chapterNumber = int(input("Enter Chapter: "))
        break
    except ValueError:
        print("Please enter a valid chapter number.")

# Get summary from the user.
summary = input("Enter Summary: ")

# Create the BookManager.
bookManager = BookManager()

book = bookManager.getValidBook(bookName, chapterNumber)

# Error condition if reference is invalid.
if book is None:
    print(f"'{bookName} {chapterNumber}' is not a valid Bible reference.")
    exit()

# Create the Chapter object.
chapter = Chapter(book.name, chapterNumber, summary)

# Create the Markdown study note.
createStudyNote(chapter)

# Save the JSON data.
jsonPath = f"{chapter.getFolderName()}/{chapter.getJsonFileName()}"
saveChapterData(jsonPath, chapter.toDictionary())

# Load the JSON back for testing.
loadedChapter = loadChapterData(jsonPath)

print("\nData loaded from JSON:")
print(loadedChapter)