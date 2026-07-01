import json
from pathlib import Path
from datetime import datetime

folder_path = Path("data/raw")

folder_path.mkdir(parents=True, exist_ok=True)

def save_raw_json(proj_name: str, data):
    """Store raw json data in the `data/raw` directory."""
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")

    file_name = folder_path / f"{proj_name}_{date}.json"

    if data:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully written to {file_name} file")
        return file_name
    else:
        print("Failed to fetch data")
        return None