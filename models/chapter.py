from config import BIBLE_FOLDER

class Chapter:

    def __init__(self, book, chapter, summary):
        #Attributes. Can access as: chapter.book=book vs chapter["book"]
        self.book = book
        self.chapter = chapter
        self.summary = summary

        self.people = []
        self.themes = []

    # Instance methods to return fileName, json file name, and folder name.
    def getFileName(self):
        return f"{self.book}{self.chapter}.md"
    
    def getJsonFileName(self):
        return f"{self.book}{self.chapter}.json"
    
    def getFolderName(self):
        return f"{BIBLE_FOLDER}/{self.book}"
    
    # Instance method of Chapter class to return a standard Python dictionary
    def toDictionary(self):
        return {
            "book": self.book,
            "chapter": self.chapter,
            "summary": self.summary,
            "people": self.people,
            "themes": self.themes
        }