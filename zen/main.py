import arguments, logs, settings, domain

def main():
    args = arguments.get()
    

    match args.command:
        case "log":
            logs.handle(args)
        case "domain":
            domain.handle(args)
            
        


if __name__ == "__main__":
    main()