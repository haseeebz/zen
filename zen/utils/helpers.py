from pathlib import Path
import os, shutil
from datetime import datetime
from zen import config


def ask_user(msg: str, options: list[str]) -> str:

    while True:
        choice = input(f"{msg} {tuple(options)} : ")

        if choice in options:
            return choice
        
        print("Incorrect option!")
        

def get_logfile_from_date(date: datetime) -> Path:
    logfile = Path(str(date.year)) / str(date.month) / f"{date.day}.log"
    return logfile





