from managers.fileManager import createFolder

# Takes a chapter name and a summary and puts it into a markdown file.
def createStudyNote(chapter):

    # Create folder path in Bible/1Chronicles folder.
    #folderPath = createFolder(f"Bible/{bookName}")
    folderPath = createFolder(chapter.getFolderName())

    #filePath = folderPath / fileName
    filePath = folderPath / chapter.getFileName()

    # Open created file path ("w" = write)
    with open(filePath, "w") as file:
        file.write(f"# {chapter.book} Chapter {chapter.chapterNumber}\n\n")

        file.write("## Summary\n\n")
        file.write(chapter.studyData.summary + "\n\n")

        file.write("## People\n\n")
        for person in chapter.studyData.people:
            file.write(f"- {person}\n")

        file.write("\n## Places\n\n")
        for place in chapter.studyData.places:
            file.write(f"- {place}\n")

        file.write("\n## Themes\n\n")
        for theme in chapter.studyData.themes:
            file.write(f"- {theme}\n")

        file.write("\n## Cross References\n\n")
        for reference in chapter.studyData.crossReferences:
            file.write(f"- {reference}\n")

        file.write("\n## Applications\n\n")
        for application in chapter.studyData.applications:
            file.write(f"- {application}\n")

    # Print success message
    print(f"Created {filePath}")