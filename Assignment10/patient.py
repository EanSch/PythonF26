
class Patient:
    # --- 1. Initializer --------------------------------------------
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # --- 2. Accessor (getter) methods -------------------------------
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    # --- 3. Mutator (setter) methods --------------------------------
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    # --- 4. __str__ -------------------------------------------------
    def __str__(self):
        return (f"Patient Name: {self.__name}\n"
                f"Address: {self.__address}\n"
                f"Phone: {self.__phone}")
