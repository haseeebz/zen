from pathlib import Path
import os

def check_log_dir():
    parent = Path(__file__).resolve().parents[1]

    log_dir = parent / "logs"

    if not log_dir.exists():
        os

    


check_log_dir()