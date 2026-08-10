import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# -------------- File structure --------------------
OUTPUT_ROOT = r"C:\All Folders\BibleStudyVault\BibleStudies"

BIBLE_FOLDER = "Bible"

BIBLE_BOOKS_FILE = "Bible/books.json"

DEFAULT_NOTE_EXTENSION = ".md"

DEFAULT_DATA_EXTENSION = ".json"

PROMPTS_FOLDER = "prompts"

# -------------- AI --------------------
AI_PROVIDER = "gemini"

GEMINI_MODEL = "gemini-3.5-flash"

AI_TEMPERATURE = 0.7

AI_MAX_OUTPUT_TOKENS = 1200

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Load Gemini API key from environment variable