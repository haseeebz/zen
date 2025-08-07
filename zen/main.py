import arguments, logs, settings

def main():
    args = arguments.get()
    

    match args.command:
        case "log":
            logs.log(args)
            
        


if __name__ == "__main__":
    main()