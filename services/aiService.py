"""
aiService.py

Purpose:
    Coordinates AI study generation.

Primary Class:
    AIService
"""

from exceptions import AIProviderError
from providers.providerFactory import ProviderFactory
from services.promptBuilder import PromptBuilder


class AIService:
    """
    Purpose:
        Coordinates AI-generated Bible study content.

    Responsibilities:
        - Create prompts.
        - Send prompts to the configured AI provider.
        - Return generated study data.

    Workflow:
        1. Receive validated Bible reference.
        2. Build AI prompt.
        3. Send prompt to provider.
        4. Return generated study.

    Methods:
        - __init__()
        - generateStudy()
    """

    def __init__(self):
        """
        Creates the AI service.

        Parameters:
            None

        Returns:
            None
        """

        self.provider = ProviderFactory.createProvider()
        self.promptBuilder = PromptBuilder()

    def generateStudy(self, book, chapterNumber):
        """
        Generates AI study content.

        Parameters:
            book (Book): Validated Bible book object.
            chapterNumber (int): Chapter number to generate.

        Returns:
            dict: Generated study information.

        Workflow:
            1. Create prompt.
            2. Send prompt to AI provider.
            3. Return generated content.
        """

        prompt = self.promptBuilder.buildStudyPrompt(book.name, chapterNumber)

        summary = self.provider.generate(prompt)

        return {
            "summary": summary
        }