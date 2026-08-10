from pathlib import Path
import json

from config import OUTPUT_ROOT


def saveChapterData(filePath, data):
    """
    Saves chapter data as JSON.

    Parameters:
        filePath (str): Path relative to OUTPUT_ROOT.
        data (dict): Chapter data to save.

    Returns:
        None
    """

    filePath = Path(OUTPUT_ROOT) / filePath

    filePath.parent.mkdir(parents=True, exist_ok=True)

    with open(filePath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Saved {filePath}")


def loadChapterData(filePath):
    """
    Loads chapter data from JSON.

    Parameters:
        filePath (str): Path relative to OUTPUT_ROOT.

    Returns:
        dict: Loaded chapter data.
    """

    filePath = Path(OUTPUT_ROOT) / filePath

    with open(filePath, "r", encoding="utf-8") as file:
        return json.load(file)