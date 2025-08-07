from datetime import datetime
from pathlib import Path
import helpers, os, config, domain

def get_logfile(dom: str) -> Path:
    
    if not helpers.check_log_dir():
        print("logs/ does not exist. No where to write logs to.")
        exit(1)

    date = datetime.now()
    logfile = helpers.get_logfile_from_date(date)

    if dom not in domain.get_domains():
        print(f"Domain '{dom}' does not exist!")
        exit(1)

    logfile = config.LOG_DIR / dom / logfile

    if not logfile.exists():
        directories = os.path.dirname(logfile)
        os.makedirs(directories, exist_ok=True)
        open(logfile, "x").close()
            
    return logfile   


def log(msg: str, domain: str | None):

    if not domain:
        print("Domain not specified!")
        exit(1)
             
    logfile = get_logfile(domain)

    with open(logfile, "a") as file:
        file.write(msg + "\n")


def handle(args):

    if args.message:
        log(args.message, args.domain)

