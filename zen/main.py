from zen import arguments, logs, domain, read


def main():
    args = arguments.get()
    
    match args.command:
        case "log":
            logs.handle(args)
        case "domain":
            domain.handle(args)
        case "read":
            read.handle(args)

            
        


if __name__ == "__main__":
    main()