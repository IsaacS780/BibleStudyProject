"""
promptBuilder.py

Purpose:
    Loads prompt templates and fills them with data.

Methods:
    - buildStudyPrompt()
"""

from pathlib import Path
from string import Template

from config import PROMPTS_FOLDER


class PromptBuilder:
    """
    Purpose:
        Builds prompts from Markdown template files.

    Methods:
        - buildStudyPrompt()
    """

    def buildStudyPrompt(self, bookName, chapterNumber):
        """
        Builds the study prompt.

        Parameters:
            bookName (str): Bible book name.
            chapterNumber (int): Chapter number.

        Returns:
            str: Completed prompt.
        """

        promptPath = Path(PROMPTS_FOLDER) / "studyPrompt.md"

        with open(promptPath, "r", encoding="utf-8") as file:
            template = Template(file.read())

        return template.substitute(book=bookName, chapter=chapterNumber)