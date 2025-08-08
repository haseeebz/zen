from pathlib import Path
import platform, os, json


if platform.system() == "Windows":
    ZEN_DIR = Path(os.environ["APPDATA"]) / "zen"
else:
    ZEN_DIR = Path(os.path.expanduser("~/.config")) / "zen"

LOG_DIR = ZEN_DIR / "logs"
SETTINGS_FILE = ZEN_DIR / "settings.json"


def create_settings_file():

    if SETTINGS_FILE.exists(): os.remove(SETTINGS_FILE)

    settings = {
        "name" : "User"
    }

    with open(SETTINGS_FILE, "x") as file:
        json.dump(settings, file)

    print(f"Created settings file: {SETTINGS_FILE}")


def initialize():

    print("Initializing zen...")

    os.mkdir(ZEN_DIR)
    os.mkdir(LOG_DIR)
    os.mkdir(LOG_DIR / "default")


    print(f"Created {ZEN_DIR}")
    create_settings_file()
    


if not ZEN_DIR.exists():
    print(f"Did not find {ZEN_DIR}.")
    initialize()
    

# Settings



ALL_SETTINGS = [
    ("source", "URL or SSH to the github repo."),
    ("default_domain", "The domain that will be accessed by default.")
]

SETTINGS = {}

class Settings():
    default_domain: str | None = None
    source: str | None = None
    zen_dir = ZEN_DIR
    log_dir = LOG_DIR
    file = SETTINGS_FILE


def load_settings():

    if not SETTINGS_FILE.exists():
        print(f"{SETTINGS_FILE} does not exist! Creating one.")
        create_settings_file()

    
    with open(SETTINGS_FILE) as file:
        try:
            settings: dict = json.load(file)
        except json.JSONDecodeError:
            print("Invalid config file. Rewriting file, try again.")
            create_settings_file()
            exit(1)

    global SETTINGS
    SETTING = settings
    Settings.default_domain = settings.setdefault("default_domain", None)
    Settings.source = settings.setdefault("source", None)



