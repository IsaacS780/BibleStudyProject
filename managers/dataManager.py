import json

def saveChapterData(filePath, chapterData):
    with open(filePath, "w") as file:
        json.dump(chapterData, file, indent=4)

    print(f"Saved {filePath}")

# Opens json file and loads into a Python dictionary
def loadChapterData(filePath):
    with open(filePath, "r") as file:
        return json.load(file)