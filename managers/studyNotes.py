from managers.fileManager import createFolder

# Takes a chapter name and a summary and puts it into a markdown file.
def createStudyNote(chapter):

    # Create folder path in Bible/1Chronicles folder.
    #folderPath = createFolder(f"Bible/{bookName}")
    folderPath = createFolder(chapter.getFolderName())

    # Create file path using chapter name given as input.
    fileName = f"{chapter.book}{chapter.chapter}.md"

    #filePath = folderPath / fileName
    filePath = folderPath / chapter.getFileName()

    # Open created file path ("w" = write)
    with open(filePath, "w") as file:
        # Write chapter name as heading.
        file.write(f"# {chapter.book} Chapter { chapter.chapter}\n")
        # Write summary into md file.
        file.write(chapter.studyData.summary)

    # Print success message
    print(f"Created {filePath}")