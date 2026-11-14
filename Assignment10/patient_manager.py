
from patient import Patient
from procedure import Procedure


def create_patient():
    """Prompt for name, address, and phone, and return a new Patient."""
    # Prompt for the patient's information.
    name = input("Enter patient name: ")
    address = input("Enter patient address: ")
    phone = input("Enter patient phone: ")

    # Create and return a Patient object.
    return Patient(name, address, phone)


def create_procedure():
    """Prompt for procedure details and return a new Procedure."""
    # Prompt for procedure information.
    description = input("Enter procedure description: ")
    date = input("Enter procedure date: ")
    practitioner = input("Enter practitioner name: ")

    # Get and validate the procedure charge.
    while True:
        try:
            charge = float(input("Enter procedure charge: "))

            if charge > 0:
                break
            else:
                print("Charge must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    # Create and return a Procedure object.
    return Procedure(description, date, practitioner, charge)


def main():
    patient = create_patient()

    procedures = []
    print("\nAdd one or more procedures (enter 'n' to stop).")

    # Allow the user to add procedures.
    while True:
        choice = input("Add a procedure? (y/n): ").lower()

        if choice == "n":
            break

        elif choice == "y":
            procedure = create_procedure()
            procedures.append(procedure)

        else:
            print("Please enter y or n.")

    # Display patient and procedure information.
    print("\nPatient and Procedure Information:")
    print(patient)

    total = 0

    for procedure in procedures:
        print()
        print(procedure)
        total += procedure.get_charge()

    # Display the total cost.
    print(f"\nTotal Cost: ${total:.2f}")


if __name__ == "__main__":
    main()
