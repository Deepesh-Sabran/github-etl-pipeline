from pathlib import Path
from extract.github_extract import fetch_git_repos
from utils.logger import write_log
from utils.save_json import save_raw_json
from transform.github_transform import transform_github_data
from utils.save_csv import save_to_csv
from report.github_report import generate_github_reports

write_log("github", "info", "Pipeline started.")

data = fetch_git_repos()

if data:
    saved_file = save_raw_json("github", data)
    write_log("github", "info", f"Successfully saved {len(data["items"])} Raw GitHub repository data to {saved_file}.")

    transformed_df = transform_github_data(data)
    csv_file = save_to_csv(Path("data/processed"), "github", transformed_df)
    write_log("github", "info", f"Successfully added required transformed data to {csv_file}.")

    generate_github_reports(transformed_df)

    write_log("github", "info", "Pipeline completed.")
else:
    write_log("github", "error", "Failed to fetch GitHub repositories.")