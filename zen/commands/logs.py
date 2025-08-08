from zen.utils import helpers
from zen.utils.settings import SETTINGS
from . import domain
from datetime import datetime
import os
from pathlib import Path

def get_logfile(dom: str) -> Path:

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
        if not SETTINGS.default_domain:
            print(f"No domain specified. No default domain found either.")
            exit(1)

        dom = SETTINGS.default_domain
             
    logfile = get_logfile(dom)

    with open(logfile, "a") as file:
        file.write(msg + "\n")

    print(f"Logged to {helpers.format_date(datetime.now())} in domain '{dom}'.")


def handle(args):
    if args.message:
        log(args.message, args.domain)

