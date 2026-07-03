# config file
import os
from dotenv import load_dotenv

load_dotenv()

# ---------------- GitHub ---------------- #

BASE_URL = "https://api.github.com"
SEARCH_REPO_URL = "/search/repositories"
TIMEOUT = 30

PARAMS = {
    "q": "is:public",
    "sort": "stars",
    "order": "desc",
    "page": 1,
    "per_page": 100
}

# ---------------- Resend ---------------- #

RESEND_BASE_URL = "https://api.resend.com"
SEND_EMAIL_URL = "/emails"

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
RESEND_FROM = os.getenv("RESEND_FROM")
RESEND_TO = os.getenv("RESEND_TO")