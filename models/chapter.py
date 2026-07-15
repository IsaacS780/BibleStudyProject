from config import BIBLE_FOLDER

class Chapter:

    def __init__(self, book, chapterNumber, studyData):
        """
        Creates a Chapter object.

        Parameters:
            book (str): Bible book name.
            chapterNumber (int): Chapter number.
            studyData (StudyData): AI-generated study data.

        Returns:
            None
        """

        self.book = book
        self.chapterNumber = chapterNumber
        self.studyData = studyData

    # Instance methods to return fileName, json file name, and folder name.
    def getFileName(self):
        return f"{self.book}{self.chapterNumber}.md"
    
    def getJsonFileName(self):
        return f"{self.book}{self.chapterNumber}.json"
    
    def getFolderName(self):
        return f"{BIBLE_FOLDER}/{self.book}"
    
    # Instance method of Chapter class to return a standard Python dictionary
    def toDictionary(self):
        return {
            "book": self.book,
            "chapter": self.chapterNumber,
            "studyData": self.studyData.toDictionary()
        }