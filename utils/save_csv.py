from pathlib import Path
from datetime import datetime

def save_to_csv(folder_path: Path, file_prefix: str, data):
    """Store transformed data to csv."""
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    folder_path.mkdir(parents=True, exist_ok=True)

    file_name = folder_path / f"{file_prefix}_{date}.csv"

    if not data.empty:
        data.to_csv(file_name, index=False)
        print(f"Successfully saved data to {file_name}.")
        return file_name
    else:
        print("Failed to fetch data")
        return None
    
    save_data.__doc__ = (
        f"""Store transformed data to csv in the '{folder_path}' directory."""
    )