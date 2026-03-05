import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
MOCK_SERVER_URL = os.getenv("MOCK_SERVER_URL")