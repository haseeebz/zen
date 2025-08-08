from datetime import datetime
import os
from pathlib import Path
from zen import helpers, config, domain, settings

def get_logfile(dom: str) -> Path:
    
    if not helpers.check_log_dir():
        print(f"{config.LOG_DIR} does not exist. No where to write logs to.")
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


def log(msg: str, dom: str | None):

    if not dom:
        if not settings.DEFAULT_DOMAIN:
            print(f"No domain specified. No default domain found either.")
            exit(1)

        dom = settings.DEFAULT_DOMAIN
             
    logfile = get_logfile(dom)

    with open(logfile, "a") as file:
        file.write(msg + "\n")


def handle(args):

    if args.message:
        log(args.message, args.domain)

