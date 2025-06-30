import os

# OpenAI API Configuration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
OPENAI_MODEL = "provider-5/chatgpt-4o-latest"

# Flask Configuration
SECRET_KEY = 'harry_potter_magic_key_2024'
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

# AI Response Configuration
MAX_TOKENS = 500
TEMPERATURE = 0.8

# Character Chat Configuration
ENABLE_AI_RESPONSES = True  # Set to False to use fallback responses
FALLBACK_RESPONSES = True   # Enable fallback if AI fails 