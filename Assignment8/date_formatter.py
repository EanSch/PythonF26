def main():
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    date = input("Enter a date (mm/dd/yyyy): ")

    parts = date.split("/")

    if len(parts) != 3:
        print("Invalid format. Please use mm/dd/yyyy.")
        return

    if not parts[0].isdigit() or not parts[1].isdigit() or not parts[2].isdigit():
        print("Invalid date. Please enter numbers only.")
        return

    month = int(parts[0])
    day = int(parts[1])
    year = parts[2]

    if month < 1 or month > 12:
        print("Invalid month. Month must be between 1 and 12.")
        return

    if day < 1 or day > 31:
        print("Invalid day. Day must be between 1 and 31.")
        return

    print(months[month - 1], str(day) + ",", year)


if __name__ == "__main__":
    main()