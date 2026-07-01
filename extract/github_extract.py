# extraction logic
import requests
from config.config import BASE_URL, SEARCH_REPO_URL, TIMEOUT, PARAMS
from utils.logger import write_log

def fetch_git_repos():
    """Fetch GitHub Repository Data with automatic retries."""
    url = BASE_URL + SEARCH_REPO_URL

    try:
        response = requests.get(url, params=PARAMS, timeout=TIMEOUT)

        if response.status_code in [401, 403, 404, 500]:
            write_log("github", "error", f"Critical error {response.status_code}. Stopping process.")
            return None
        
        if response.status_code == 200:
            write_log("github", "info", f"Data fetched successfully.")
            return response.json()
        
        write_log("github", "warn", f"First request failed ({response.status_code}). Retrying...")
        for i in range(3):
            response = requests.get(url, params=PARAMS, timeout=TIMEOUT)
            if response.status_code == 200:
                write_log("github", "info", f"Data fetched successfully.")
                return response.json()
            write_log("github", "warn", f"Retry {i+1} failed...")

        write_log("github", "error", f"Request Error after 3 retries: {response.status_code}")
        return None
        
    except Exception as e:
        write_log("github", "error", f"Exception at extract file: {e}")
        return None