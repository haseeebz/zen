import json
from typing import Any
from zen.utils import settings
from zen.utils.settings import Settings



def list_all_settings():
    for name, info in settings.ALL_SETTINGS:
        print(f"{name:<16} : {Settings.__dict__[name]} - {info}")


def set_settings(key, value):
    settings.SETTINGS[key] = value

    with open(settings.SETTINGS_FILE, 'w') as file:
        json.dump(settings.SETTINGS, file)


def handle(args):
    
    if args.list:
        list_all_settings()

    if args.set:
        set_settings(args.set[0], args.set[1])


    
    
