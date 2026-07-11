import json


chapterData = {
    "book": "1 Chronicles",
    "chapter": 8,
    "summary": "Benjamin's genealogy continues.",
    "people": [
        "Benjamin",
        "Saul"
    ],
    "themes": [
        "genealogy",
        "tribes"
    ]
}


with open("chapterData.json", "w") as file:
    json.dump(chapterData, file, indent=4)


print("Data saved successfully")

with open("chapterData.json", "r") as file:
    savedData = json.load(file)


print(savedData["book"])