from studyNotes import createStudyNote
from dataManager import saveChapterData

chapterData = {
    "book": "1Chronicles",
    "chapter": 9,
    "summary": "The genealogy of Benjamin continues.",
    "people": [
        "Benjamin"
    ],
    "themes": [
        "genealogy"
    ]
}

createStudyNote(
    chapterData["book"],
    chapterData["chapter"],
    chapterData["summary"]
)

saveChapterData(
    "chapterData.json",
    chapterData
)