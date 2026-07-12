from models.chapter import Chapter
from managers.studyNotes import createStudyNote
from managers.dataManager import saveChapterData, loadChapterData
from managers.bookManager import BookManager


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

# Retrieve the requested book.
book = bookManager.getBook(bookName)

# Validate the book.
if book is None:
    print(f"'{bookName}' is not a valid book.")
    exit()

# Validate the chapter.
if not book.isValidChapter(chapterNumber):
    print(f"Chapter {chapterNumber} does not exist in {book.name}.")
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