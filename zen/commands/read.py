from datetime import datetime
from zen.utils import helpers
from zen.utils.settings import SETTINGS
from . import domain

def get_logfile(date: str, dom: str):
    
    try:
        y, m, d = date.split("/")
        dt = datetime(int(y), int(m), int(d))
    except (ValueError, TypeError):
        print(f"Invalid date: {date}")
        exit(1)

    logfile = helpers.get_logfile_from_date(dt)
    
    if dom not in domain.get_domains():
        print(f"Domain '{dom}' does not exist!")
        exit(1)

    logfile = SETTINGS.LOG_DIR / dom / logfile

    if not logfile.exists():
        print(f"Log file for date '{date}' in domain '{dom}' does not exist!")
        print("Maybe you did'nt log that day?")
        exit(1)

    return logfile


def read(date: str, dom: str | None):

    if not dom:
        if not settings.DEFAULT_DOMAIN:
            print(f"No domain specified. No default domain found either.")
            exit(1)

        dom = settings.DEFAULT_DOMAIN
    
    logfile = get_logfile(date, dom)

    with open(logfile) as file:
        content = file.read()

    print(content)


def handle(args):

    if args.date:
        read(args.date, args.domain)