from .utils import arguments
from .commands import domain, logs, read, settings
from .utils.settings import load_settings

def main():

    args = arguments.get()
    load_settings()
    
    match args.command:
        case "log":
            logs.handle(args)
        case "domain":
            domain.handle(args)
        case "read":
            read.handle(args)
        case "setting":
            settings.handle(args)
    

if __name__ == "__main__":
    main()