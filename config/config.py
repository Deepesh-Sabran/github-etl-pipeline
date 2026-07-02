# config file

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