from pathlib import Path
from config import OUTPUT_ROOT

# Takes a folder path and ensures it exists.
def createFolder(folderPath):
    folder = Path(OUTPUT_ROOT) / folderPath

    folder.mkdir(parents=True, exist_ok=True)

    return folder