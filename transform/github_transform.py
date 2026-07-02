import pandas as pd

def transform_github_data(data):
    """Normalize JSON data and returns Dataframe with required field"""
    github_df = pd.json_normalize(data["items"])
    required_df = github_df[
        [
            "id",
            "full_name",
            "owner.login",
            "description",
            "language",
            "stargazers_count",
            "forks_count",
            "html_url",
            "created_at",
            "updated_at",
            "pushed_at",
        ]
    ]

    required_df = required_df.rename(
        columns={
            "id": "repository_id",
            "full_name": "repository_name",
            "owner.login": "owner_name",
            "stargazers_count": "stars",
            "forks_count": "forks",
            "html_url": "repository_url",
        }
    )

    return required_df