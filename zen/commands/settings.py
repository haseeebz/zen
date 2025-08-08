import json
from typing import Any
from zen.utils.settings import SETTINGS, ALL_SETTINGS, Settings



def list_all_settings():
    for name, info in ALL_SETTINGS:
        print(f"{name:<20} : {info}")


def set_settings(key, value):
    SETTINGS[key] = value

    with open(settings.SETTINGS_FILE, 'w') as file:
        json.dump(SETTINGS, file)


def handle(args):
    
    if args.list:
        list_all_settings()

    if args.set:
        set_settings(args.set[0], args.set[1])


    
    
