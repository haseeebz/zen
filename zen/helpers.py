from pathlib import Path
import os
import config

def ask_user(msg: str, options: list[str]) -> str:

    while True:
        choice = input(f"{msg} {tuple(options)} : ")

        if choice in options:
            return choice
        
        print("Incorrect option!")



def check_log_dir() -> bool:

    log_dir = config.LOG_DIR

    if not log_dir.exists():
        choice = helpers.ask_user(
            f"{log_dir} does not exist. Do you want to create it?",
            ['y', 'n']
        )

        if choice == 'y':
            os.mkdir(log_dir)
            return True
        else:
            return False


    if not log_dir.is_dir():
        choice = helpers.ask_user(
            f"{log_dir} is a file. Do you want to remove it and create a directory?",
            ['y', 'n']
        )

        if choice == 'y':
            os.remove(log_dir)
            os.mkdir(log_dir)
            return True
        else:
            return False
        

    


