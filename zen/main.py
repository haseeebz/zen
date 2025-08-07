import arguments, logs, settings, domains

def main():
    args = arguments.get()
    

    match args.command:
        case "log":
            logs.log(args)
        case "domain":
            domains.handle(args)
            
        


if __name__ == "__main__":
    main()