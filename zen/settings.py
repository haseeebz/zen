import helpers, json
from typing import Any

SETTINGS = {}


def check_settings_file():

    if config.SETTINGS_FILE.exists():
        return 

    settings = {
        "name" : "User"
    }

    with open(config.SETTINGS_FILE) as file:
        json.dump(settings, file)

    SETTINGS = settings


def get_setting(key: str) -> Any | None:
    return SETTINGS.setdefault(key, None)

    
    
    
