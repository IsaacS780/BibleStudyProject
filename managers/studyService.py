from models.chapter import Chapter
from managers.studyNotes import createStudyNote
from managers.dataManager import saveChapterData, loadChapterData

class StudyService:
    """
    Purpose:
        Coordinates the complete Bible study creation workflow.

    Current Responsibilities:
        - Create Chapter objects.
        - Generate Markdown study notes.
        - Save study data as JSON.
        - Return the saved study data.

    Future Responsibilities:
    - Generate AI study content.
    - Update character database.
    - Update place database.
    - Update timeline.
    - Generate cross references.

    Workflow:
        1. Receive validated study information.
        2. Create a Chapter object.
        3. Generate the Markdown note.
        4. Save the study as JSON.
        5. Load and return the saved data.

    Methods:
        - createStudy(book, chapterNumber, summary)
    """

    def createStudy(self, book, chapterNumber, summary):
        """
        Creates a complete Bible study.

        Parameters:
            book (Book): The validated Bible book.
            chapterNumber (int): The chapter to study.
            summary (str): The summary text for the chapter.

        Returns a dictionary with the saved chapter data loaded from the JSON file.

        Workflow:
            1. Create a Chapter object.
            2. Generate the Markdown note.
            3. Save the chapter data.
            4. Load the saved data.
            5. Return the loaded data.
        """
         
        # Create the Chapter object.
        chapter = Chapter(book.name, chapterNumber, summary)

        # Create the Markdown study note.
        createStudyNote(chapter)

        # Save the study data.
        jsonPath = f"{chapter.getFolderName()}/{chapter.getJsonFileName()}"
        saveChapterData(jsonPath, chapter.toDictionary())

        # Load and return the saved data.
        return loadChapterData(jsonPath)