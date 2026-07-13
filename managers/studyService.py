from models.chapter import Chapter
from managers.studyNotes import createStudyNote
from managers.dataManager import saveChapterData, loadChapterData

class StudyService:
#Class to manage the study process, including creating study notes and saving/loading chapter data.
    def createStudy(self, book, chapterNumber, summary):
        chapter = Chapter(book.name, chapterNumber, summary)

        createStudyNote(chapter)

        jsonPath = f"{chapter.getFolderName()}/{chapter.getJsonFileName()}"

        saveChapterData(jsonPath, chapter.toDictionary())

        return loadChapterData(jsonPath)