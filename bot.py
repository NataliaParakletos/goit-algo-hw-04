def parse_input(user_input): 
    cmd, *args = user_input.split() 
    cmd = cmd.strip().lower() 
    return cmd, args

def add_contact(args, contacts): 
    name, phone = args 
    contacts[name] = phone 
    return "Contact added." 

def change_contact(args, contacts): 
    name, new_phone = args 
    contacts[name] = new_phone 
    return "Contact updated." 

def show_phone(args, contacts): 
    name = ''.join(args)
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return "Contact not found."
    
def show_all(contacts):
    result = "Contacts list:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

def main(): 
    contacts = {} 
    print("Welcome to the assistant bot!") 
    while True: 
        user_input = input("Enter a command: ") 
        command, args = parse_input(user_input) 

        if command in ["close", "exit"]: 
            print("Good bye!") 
            break 
        elif command == "hello": 
            print("How can I help you?") 
        elif command == "add": 
            print(add_contact(args, contacts)) 
        elif command == "update": 
            print(change_contact(args, contacts)) 
        elif command == "phone_username" and args: 
            print(show_phone(args, contacts)) 
        elif command == "all": 
            print(show_all(contacts))
        else: 
            print("Invalid command.") 

if __name__ == "__main__": 
    main()