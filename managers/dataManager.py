import json

def saveChapterData(filePath, chapterData):
    with open(filePath, "w") as file:
        json.dump(chapterData, file, indent=4)

    print(f"Saved {filePath}")