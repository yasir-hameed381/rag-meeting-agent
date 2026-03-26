import os
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
CALENDAR_EMAIL = os.getenv("CALENDAR_EMAIL")