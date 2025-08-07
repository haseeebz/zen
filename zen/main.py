import arguments, logs

def main():
    args = arguments.get()

    match args.command:
        case "log":
            logs.log(args)
            
        


if __name__ == "__main__":
    main()