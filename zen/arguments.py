import argparse

def setup():

    parser = argparse.ArgumentParser("zen")
    subparser = parser.add_subparsers(
        dest = "command", 
        help = "Command you want to execute." ,
        required = True
    )


    log_parser = subparser.add_parser("log", help = "Log an entry.")
    log_parser.add_argument("message", help = "Content you want to log.")
    log_parser.add_argument("--domain", help = "Domain you want to log in.")

    read_parser = subparser.add_parser("read", help = "Log an entry.")
    read_parser.add_argument("date", help = "The date of the log file in YY/MM/DD format.")
    read_parser.add_argument("--domain", help = "Domain you want to log in.")

    domain_parser = subparser.add_parser("domain", help = "Domain operations.")
    domain_parser.add_argument("--create", help = "Create a new domain.", type=str)
    domain_parser.add_argument("--delete", help = "Delete a domain.", type=str)
    domain_parser.add_argument("--list", help = "List all domains.", action="store_true")


    return parser



def get():
    parser = setup()
    args = parser.parse_args()
    return args

