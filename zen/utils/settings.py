from pathlib import Path
import platform, os, json


if platform.system() == "Windows":
    ZEN_DIR = Path(os.environ["APPDATA"]) / "zen"
else:
    ZEN_DIR = Path(os.path.expanduser("~/.config")) / "zen"

LOG_DIR = ZEN_DIR / "logs"
SETTINGS_FILE = ZEN_DIR / "settings.json"


def initialize():

    print("Initializing zen...")

    os.mkdir(ZEN_DIR)
    os.mkdir(LOG_DIR)
    os.mkdir(LOG_DIR / "default")
    

    if SETTINGS_FILE.exists(): os.remove(SETTINGS_FILE)

    settings = {
        "name" : "User"
    }

    with open(SETTINGS_FILE, "x") as file:
        json.dump(settings, file)

    print(f"Created {ZEN_DIR}")
    print(f"Created settings file: {SETTINGS_FILE}")


if not ZEN_DIR.exists():
    print(f"Did not find {ZEN_DIR}.")
    initialize()
    

# Settings

class Settings():
    def __init__(self):
        self.default_domain: str | None = None
        self.source: str | None = None

SETTINGS = Settings()


def load_settings():

    if not SETTINGS_FILE.exists():
        print(f"{config.SETTINGS_FILE} does not exist!")
        config.configure_settings()

    with open(config.SETTINGS_FILE) as file:
        try:
            settings: dict = json.load(file)
        except json.JSONDecodeError:
            print("Invalid config file. Rewriting file, try again.")
            config.configure_settings()
            exit(1)

    global SETTINGS
    SETTINGS.default_domain = settings.setdefault("default_domain", None)
    SETTINGS.source = settings.setdefault("source", None)

