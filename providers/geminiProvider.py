"""
geminiProvider.py

Purpose:
    Creates a client that communicates with the Gemini API.

Methods:
    - generate()
"""

from urllib import response

import config

from google import genai
from google.genai import types
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
                contents=prompt,
                config = types.GenerateContentConfig(response_mime_type = "application/json")
            )

            # DEBUG CODE TO REMOVE LATER
            #print("1",type(response))
            #print("2", response)
            #print("3", response.text)

            return response.text.strip()
        
        except Exception as error:
            raise AIProviderError(f"Error generating content from Gemini: {error}")