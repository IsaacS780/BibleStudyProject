from fileManager import createFolder

# Takes a chapter name and a summary and puts it into a markdown file.
def createStudyNote(bookName, chapterNumber, summary):

    # Create folder path in Bible/1Chronicles folder.
    folderPath = createFolder(f"Bible/{bookName}")

    # Create file path using chapter name given as input.
    fileName = f"{bookName}{chapterNumber}.md"

    filePath = folderPath / fileName

    # Open created file path ("w" = write)
    with open(filePath, "w") as file:
        # Write chapter name as heading.
        file.write(f"# {bookName} Chapter { chapterNumber}\n")
        # Write summary into md file.
        file.write(summary)

    # Print success message
    print(f"Created {filePath}")