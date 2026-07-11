# This program reads a Bible study note

fileName = "1Chronicles6.md"

with open(fileName, "r") as file:
    contents = file.read()

wordCount = len(contents.split())

print("Study Note:")
print(contents)

print()
print(f"Word count: {wordCount}")