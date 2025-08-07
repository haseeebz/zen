import json
from typing import Any
from zen import helpers, config

SETTINGS = {}

ALL_SETTINGS = [
    ("source", "URL or SSH to the github repo."),
    ("default_domain", "The domain that will be accessed by default.")
]

def check_settings_file():

    if config.SETTINGS_FILE.exists():
        return 

    with open(config.SETTINGS_FILE, 'w') as file:
        json.dump(settings, file)

    SETTINGS = settings


def get_setting(key: str) -> Any | None:
    return SETTINGS.setdefault(key, None)


def list_all_settings():
    for name, info in ALL_SETTINGS:
        print(f"{name:<20} : {info}")


def set_settings(key, value):
    SETTINGS[key] = value

    with open(config.SETTINGS_FILE, 'w') as file:
        json.dump(SETTINGS, file)


def handle(args):
    
    if args.list:
        list_all_settings()

    if args.set:
        set_settings(args.set[0], args.set[1])


    
    
