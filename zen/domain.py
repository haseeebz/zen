from zen import helpers, config
import os, shutil


def create_domain(name: str):
    
    if not helpers.check_log_dir():
        print("logs/ does not exist. Cannot do operation.")
        exit(1)

    domain_dir = config.LOG_DIR / name

    if not domain_dir.exists():
        os.mkdir(domain_dir)
        print(f"Created new domain: {name}")
    else:
        print(f"Domain '{name}' already exists.")


def delete_domain(name: str):
    
    if not helpers.check_log_dir():
        print("logs/ does not exist. Cannot do operation.")
        exit(1)

    domain_dir = config.LOG_DIR / name

    if not domain_dir.exists():
        print(f"Domain '{name}' does not exist, So won't be deleted.")
    else:
        choice = helpers.ask_user(f"Are you sure you want to delete domain '{name}'? ", ["y", "n"])

        if choice == "y":
            shutil.rmtree(domain_dir)
            print(f"Domain '{name}' deleted.")
        else:
            print("Abort.")


def get_domains() -> list[str]:
    return [x.name for x in config.LOG_DIR.iterdir()]


def list_domains():
    print("Existing Domains: ")
    for item in get_domains():
        print(f"   {item}")


def handle(args):

    if args.list:
        list_domains()

    if args.create:
        create_domain(args.create)
    
    if args.delete:
        delete_domain(args.delete)
    
