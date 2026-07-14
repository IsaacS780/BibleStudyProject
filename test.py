import os
from providers.geminiProvider import GeminiProvider
from google import genai

#client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#or model in client.models.list():
#    print(model.name)

#provider = GeminiProvider()

#response = provider.generate("In one sentence, what is Genesis about?")

#print(response)
print(os.getenv("GEMINI_API_KEY"))