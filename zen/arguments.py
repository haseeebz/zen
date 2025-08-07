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


    return parser



def get():
    parser = setup()
    args = parser.parse_args()
    return args

print(get().command)