from models.chapter import Chapter
from managers.studyNotes import createStudyNote
from managers.dataManager import saveChapterData

# Get user input for what to study
book = input("Enter book: ")

# Get chapter number: Must be an integer value.
while True:
    try:
        chapterNumber = int(input("Enter Chapter: "))
        break
    except ValueError:
        print("Please enter a valid chapter number.")
# Get summary value from user.
summary = input("Enter Summary: ")

# Creates chapter data.
chapter = Chapter(book, chapterNumber, summary)

# Creates study note markdown file.
createStudyNote(chapter)

jsonPath = f"{chapter.getFolderName()}/{chapter.getJsonFileName()}"

# Convert the Chapter object to a dictionary because the JSON module
# cannot serialize custom Python objects directly.
saveChapterData(jsonPath, chapter.toDictionary())