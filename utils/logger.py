from pathlib import Path
from datetime import datetime

folder_path = Path("logs")

folder_path.mkdir(parents=True, exist_ok=True)

VALID_LEVELS = {"INFO", "WARN", "ERROR"}

def write_log(file_prefix: str, level: str, message: str):
    """Store execution logs in the `logs/` directory."""
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    date = now.strftime("%Y-%m-%d")

    file_name = f"logs/{file_prefix}_{date}.log"

    if level.upper() not in VALID_LEVELS:
        raise ValueError(f"Enter a valid level as 'info / warn / error'")
    else:
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(f"{formatted_time} | {level.upper()} | {message}\n")