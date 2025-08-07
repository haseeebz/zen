from pathlib import Path
import platform, os, json


if platform.system() == "Windows":
    ZEN_DIR = Path(os.environ["APPDATA"]) / "zen"
else:
    ZEN_DIR = Path(os.path.expanduser("~/.config")) / "zen"

LOG_DIR = ZEN_DIR / "logs"
SETTINGS_FILE = ZEN_DIR / "settings.json"


def configure():

    print(f"Did not find {ZEN_DIR}. Initializing...")
    os.mkdir(ZEN_DIR)
    os.mkdir(LOG_DIR)
    os.mkdir(LOG_DIR / "default")

    settings = {
        "name" : "User"
    }

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file)


if not ZEN_DIR.exists():
    configure()
    

