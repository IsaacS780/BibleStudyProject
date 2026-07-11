from pathlib import Path

def createStudyNote(chapterName, summary):
    folderPath = Path("Bible/1Chronicles")

    folderPath.mkdir(parents=True, exist_ok=True)

    filePath = folderPath / f"{chapterName}.md"

    with open(filePath, "w") as file:
        file.write(f"# {chapterName}\n")
        file.write(summary)

    print(f"Created {filePath}")

summary = """
1 Chronicles 6 explains the genealogy of Levi,
the priestly line of Aaron, and the Levitical cities.
"""

createStudyNote("1Chronicles6", summary)

createStudyNote("1Chronicles7", "Geneology of the tribes of Israel.")