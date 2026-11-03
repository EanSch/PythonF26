def main():
    password = input("Enter a password: ")

    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit.")

    if not password.isalnum():
        errors.append("Password may only contain letters and digits.")

    if len(errors) == 0:
        print("Password meets all requirements!")
    else:
        print("Password does not meet the requirements:")
        for error in errors:
            print("-", error)


if __name__ == "__main__":
    main()