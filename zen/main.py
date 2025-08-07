from zen import arguments, logs, domain, read, settings


def main():
    args = arguments.get()
    settings.check_settings_file()
    
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