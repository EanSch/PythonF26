import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Always read/write email.dat next to this script, regardless of the
# folder the program is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')


def main():
    """Load the emails, run the menu loop, and save after each change."""
    # TODO - Load emails, then loop reading a choice and calling the
    #        matching function below until the user quits, saving after
    #        add/change/delete.
    emails = load_emails()
    while True:
        choice = get_user_choice()
        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
            save_emails(emails)
        elif choice == CHANGE:
            change(emails)
            save_emails(emails)
        elif choice == DELETE:
            delete(emails)
            save_emails(emails)
        elif choice == QUIT:
            break


def load_emails():
    """Load and return the saved emails dictionary (or an empty one)."""
    # TODO - Unpickle FILENAME; return an empty dict if it doesn't exist
    #        or is empty.
    if os.path.exists(FILENAME):
        with open(FILENAME, 'rb') as f:
            emails = pickle.load(f)
    else:
        emails = {}
    return emails


def get_user_choice():
    """Display the menu and return a validated choice."""
    # TODO - Print the menu, read a choice, and keep re-prompting until
    #        it's a valid menu option.
    while True:
        print("1. Look up an email")
        print("2. Add an email")
        print("3. Change an email")
        print("4. Delete an email")
        print("5. Quit")
        try:
            choice = int(input("Enter your choice: "))
            if choice in [LOOK_UP, ADD, CHANGE, DELETE, QUIT]:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def look_up(emails):
    """Print the email address for a name the user enters, if found."""
    # TODO - Implement this function.
    name = input("Enter the name to look up: ")
    if name in emails:
        print("Email address:", emails[name])
    else:
        print("Name not found.")


def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    # TODO - Implement this function.
    name = input("Enter the name to add: ")
    if name in emails:
        print("Name already exists.")
    else:
        email = input("Enter the email address: ")
        emails[name] = email


def change(emails):
    """Update the address for an existing name."""
    # TODO - Implement this function.
    name = input("Enter the name to change: ")
    if name in emails:
        email = input("Enter the new email address: ")
        emails[name] = email
    else:
        print("Name not found.")


def delete(emails):
    """Remove a name/address pair."""
    # TODO - Implement this function.
    name = input("Enter the name to delete: ")
    if name in emails:
        del emails[name]
    else:
        print("Name not found.")


def save_emails(emails):
    """Pickle the emails dictionary to FILENAME."""
    # TODO - Implement this function.
    with open(FILENAME, 'wb') as f:
        pickle.dump(emails, f)


if __name__ == '__main__':
    main()
