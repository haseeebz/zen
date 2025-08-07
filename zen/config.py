from pathlib import Path
import platform, os

def configure():
    
    print(f"Did not find {ZEN_DIR}. Initializing...")
    os.mkdir(ZEN_DIR)
    os.mkdir(LOG_DIR)

    settings = {
        "name" : "User"
    }

    with open(SETTINGS_FILE) as file:
        json.dump(settings, file)


if platform.system == "Windows":
    ZEN_DIR = Path(os.environ("appdata")) / "zen"
else:
    ZEN_DIR = Path(os.path.expanduser("~/.config")) / "zen"

LOG_DIR = ZEN_DIR / "logs"
SETTINGS_FILE = ZEN_DIR / "settings.json"

if not ZEN_DIR.exists():
    configure()
    

