class Book:
    
    def __init__(self, name, chapters, canon):
        self.name = name
        self.chapters = chapters
        self.canon = canon

    # Checks whether a requested chapter exists for this specific book.
    def isValidChapter(self, chapterNumber):
        return 1 <= chapterNumber <= self.chapters
    