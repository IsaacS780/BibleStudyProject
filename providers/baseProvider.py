"""
baseProvider.py

Purpose:
    Defines the common interface for all AI providers.

Methods:
    - generate(prompt)
"""


class BaseProvider:
    """
    Base class for every AI provider.
    """

    def generate(self, prompt):
        """
        Generates a response from an AI provider.

        Parameters:
            prompt (str): Prompt sent to the provider.

        Returns:
            str: Generated response.

        Raises:
            NotImplementedError if a provider does not implement this method.
        """

        raise NotImplementedError("AI providers must implement generate().")