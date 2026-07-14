"""
providerFactory.py

Purpose:
    Creates the configured AI provider.

Methods:
    - createProvider()
"""

from config import AI_PROVIDER
from providers.geminiProvider import GeminiProvider

class ProviderFactory:
    """
    Creates AI provider instances.
    """

    @staticmethod
    def createProvider():
        """
        Creates the configured AI provider.

        Parameters: None

        Returns:
            BaseProvider: Configured AI provider.
        """

        if AI_PROVIDER == "gemini":
            return GeminiProvider()

        raise ValueError(f"Unsupported AI provider: {AI_PROVIDER}")