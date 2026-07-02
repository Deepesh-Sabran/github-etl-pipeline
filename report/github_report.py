from pathlib import Path
from utils.save_csv import save_to_csv
from utils.logger import write_log

REPORT_FOLDER = Path("reports")

# 1. Which programming languages are trending?
def trending_languages(df):
    trend_langs = (
        df["language"]
        .value_counts()
        .reset_index()
        .rename(columns={"count": "repository_count"})
    )

    saved_file = save_to_csv(REPORT_FOLDER, "github_trending_languages", trend_langs)
    write_log("github", "info", f"Report generated successfully at {saved_file}")


# 2. Which repositories are getting the most stars?
def top_repositories(df):
    top_repos = (
        df[["repository_name", "stars"]]
        .sort_values(by="stars", ascending=False)
    )

    saved_file = save_to_csv(REPORT_FOLDER, "github_top_repositories", top_repos)
    write_log("github", "info", f"Report generated successfully at {saved_file}")


# 3. Which owners created the most popular repositories?
def top_owners(df):
    owners = (
        df.groupby("owner_name")[["stars"]]
        .sum()
        .reset_index()
        .sort_values(by="stars", ascending=False)
        .rename(columns={"stars": "star_counts"})
    )

    saved_file = save_to_csv(REPORT_FOLDER, "github_top_owners", owners)
    write_log("github", "info", f"Report generated successfully at {saved_file}")


# 4. How many repositories were created each day?
def repositories_created_each_day(df):
    repos_created = (
        df["created_at"].str.split("T")
        .str[0]
        .value_counts()
        .reset_index()
        .rename(columns={"count": "repository_count"})
    )

    saved_file = save_to_csv(REPORT_FOLDER, "github_repositories_created_each_day", repos_created)
    write_log("github", "info", f"Report generated successfully at {saved_file}")


# 5. Which repositories crossed 1000 stars?
def repositories_above_1000_stars(df):
    repos = (
        df.loc[
            df["stars"] > 1000,
            ["repository_name", "stars"]
        ]
        .rename(columns={"stars": "star_count"})
    )

    saved_file = save_to_csv(REPORT_FOLDER, "github_repositories_above_1000_stars", repos)
    write_log("github", "info", f"Report generated successfully at {saved_file}")


# orchestrator function:
def generate_github_reports(df):
    trending_languages(df)
    top_repositories(df)
    top_owners(df)
    repositories_created_each_day(df)
    repositories_above_1000_stars(df)