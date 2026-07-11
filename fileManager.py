from pathlib import Path

# Takes a folder path and ensures it exists.
def createFolder(folderPath):
    folder = Path(folderPath)

    folder.mkdir(parents=True, exist_ok=True)

    return folder