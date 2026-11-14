
class Pet:
    # --- 1. Initializer --------------------------------------------
    # Runs automatically when a new Pet object is created.
    # Sets up the private data attributes.
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # --- 2. Accessor (getter) methods -------------------------------
    # Return the values of private attributes without changing them.
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    # --- 3. Mutator (setter) methods --------------------------------
    # Change the values of private attributes.
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # --- 4. __str__ -------------------------------------------------
    # Returns a string describing the object's current state.
    def __str__(self):
        return (f"Pet name: {self.__name}\n"
                f"Animal type: {self.__animal_type}\n"
                f"Age of pet: {self.__age}")
