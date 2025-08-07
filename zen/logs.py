from datetime import datetime
from pathlib import Path
import helpers, os, config

def get_logfile() -> Path:
    
    if not helpers.check_log_dir():
        print("logs/ does not exist. No where to write logs to.")
        exit(1)

    date = datetime.now()
    logfile = helpers.get_logfile_from_date(date)

    logfile = config.LOG_DIR / logfile

    if not logfile.exists():
        directories = os.path.dirname(logfile)
        os.makedirs(directories, exist_ok=True)
        open(logfile, "x").close()
            
    return logfile   


def log(args):
    
    logfile = get_logfile()

    with open(logfile, "a") as file:
        file.write(args.message)

     