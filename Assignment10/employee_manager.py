
import pickle
from employee import Employee


FILENAME = "employees.dat"


# --- 1. File methods -----------------------------------------------
# Load employee information from the file.
def load_employees():
    try:
        with open(FILENAME, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


# Save employee information to the file.
def save_employees(employees):
    with open(FILENAME, "wb") as file:
        pickle.dump(employees, file)


# --- 2. Look up an employee ----------------------------------------
def look_up_employee(employees):
    id_number = input("Enter an employee ID number: ")

    if id_number in employees:
        print(employees[id_number])
    else:
        print("The specified ID number was not found")


# --- 3. Add a new employee -----------------------------------------
def add_employee(employees):
    name = input("Enter employee name: ")
    id_number = input("Enter employee ID number: ")
    department = input("Enter employee department: ")
    title = input("Enter employee title: ")

    employee = Employee(name, id_number, department, title)
    employees[id_number] = employee

    save_employees(employees)
    print("The new employee has been added.")


# --- 4. Change an existing employee -------------------------------
def change_employee(employees):
    id_number = input("Enter employee ID number: ")

    if id_number in employees:
        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        title = input("Enter the new title: ")

        employee = employees[id_number]
        employee.set_name(name)
        employee.set_department(department)
        employee.set_title(title)

        save_employees(employees)
        print("Employee information updated.")
    else:
        print("The specified ID number was not found")


# --- 5. Delete an employee -----------------------------------------
def delete_employee(employees):
    id_number = input("Enter employee ID number: ")

    if id_number in employees:
        del employees[id_number]
        save_employees(employees)
        print("Employee information deleted.")
    else:
        print("The specified ID number was not found")


# --- 6. Main --------------------------------------------------------
def main():
    employees = load_employees()

    choice = 0

    while choice != 5:
        print("\nMenu")
        print("--------------------------------------")
        print("1. Look up an employee")
        print("2. Add a new employee")
        print("3. Change an existing employee")
        print("4. Delete an employee")
        print("5. Quit the program")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            look_up_employee(employees)

        elif choice == 2:
            add_employee(employees)

        elif choice == 3:
            change_employee(employees)

        elif choice == 4:
            delete_employee(employees)

        elif choice == 5:
            print("Goodbye!")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
