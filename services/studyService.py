from models import book
from models.chapter import Chapter
from managers.studyNotes import createStudyNote
from managers.dataManager import saveChapterData, loadChapterData
from services.aiService import AIService

class StudyService:
    """
    Purpose:
        Coordinates the complete Bible study creation workflow.

    Current Responsibilities:
        - Generate AI study content.
        - Create Chapter objects.
        - Generate Markdown study notes.
        - Save study data as JSON.
        - Return the saved study data.

    Future Responsibilities:
        - Update character database.
        - Update place database.
        - Update timeline.
        - Generate cross references.

    Workflow:
        1. Receive validated Bible information.
        2. Request AI-generated study content.
        3. Create a Chapter object.
        4. Generate the Markdown note.
        5. Save the study as JSON.
        6. Load and return the saved data.

    Methods:
        - createStudy(book, chapterNumber)
    """

    def __init__(self):
        """
        Creates the StudyService and initializes the AIService.

        Parameters: None

        Returns: None
        """

        self.aiService = AIService()

    def createStudy(self, book, chapterNumber):
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
         
        studyData = self.aiService.generateStudy(book, chapterNumber)

        chapter = Chapter(book.name, chapterNumber, studyData["summary"])

        # Create the Markdown study note.
        createStudyNote(chapter)

        # Save the study data.
        jsonPath = f"{chapter.getFolderName()}/{chapter.getJsonFileName()}"
        saveChapterData(jsonPath, chapter.toDictionary())

        # Load and return the saved data.
        return loadChapterData(jsonPath)