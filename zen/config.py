from pathlib import Path

PARENT_DIR = Path(__file__).resolve().parents[1]
ZEN_DIR = Path(__file__).resolve().parent
LOG_DIR = PARENT_DIR / "logs"

SETTINGS_FILE = ZEN_DIR / "settings.json"
