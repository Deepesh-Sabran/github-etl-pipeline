from extract.github_extract import fetch_git_repos
from utils.logger import write_log
from utils.save_json import save_raw_json

write_log("github", "info", "Pipeline started.")

data = fetch_git_repos()

if data:
    saved_file = save_raw_json("github", data)
    write_log("github", "info", f"Successfully saved {len(data["items"])} Raw GitHub repository data to {saved_file}.")
    write_log("github", "info", "Pipeline completed.")
else:
    write_log("github", "error", "Failed to fetch GitHub repositories.")