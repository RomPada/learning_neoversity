def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Контакт {name} не знайдено"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Команди: add <name> <phone>, show <name>, all, exit (close)")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "show":
            print(show_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
