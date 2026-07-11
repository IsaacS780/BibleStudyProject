# This program creates a simple Bible study note

chapter = "1 Chronicles 6"

summary = """
1 Chronicles 6 explains the genealogy of Levi,
the priestly line of Aaron, and the Levitical cities.
"""

file_name = "1Chronicles6.md"

with open(file_name, "w") as file:
    file.write(f"# {chapter}\n")
    file.write(summary)

print(f"Created {file_name}")