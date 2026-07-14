"""
geminiProvider.py

Purpose:
    Creates a client that communicates with the Gemini API.

Methods:
    - generate()
"""

import config

from google import genai
from exceptions import AIProviderError

class GeminiProvider:
    """
    Handles communication with Gemini.
    """

    def __init__(self):
        """
        Creates the Gemini client.

        Parameters: None

        Returns: None
        """

        self.client = genai.Client(api_key=config.GEMINI_API_KEY)

    def generate(self, prompt):
        """
        Sends a prompt to Gemini.

        Parameters:
            prompt (str): Prompt text.

        Returns:
            str: Generated response.
        """

        try: 
            # Sends a request to Gemini and returns the generated content.
            response = self.client.models.generate_content(
                model = config.GEMINI_MODEL,
                contents=prompt
            )

            return response.text
        
        except Exception as error:
            raise AIProviderError(f"Error generating content from Gemini: {error}")