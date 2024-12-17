import os
from dotenv import load_dotenv

load_dotenv()

USER_API_TOKEN = os.getenv("USER_API_TOKEN")
BASE_FB_URL = os.getenv("BASE_FB_URL")
PAGES = [
    {"id": os.getenv("PAGE_1_ID"), "token": os.getenv("PAGE_1_TOKEN")},
]
