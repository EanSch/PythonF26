# TODO: define Global Constants
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)

# TODO: complete this function which prompt user for the temperature type (C or F) until a valid input is received.
def get_temperature_type():
    temp_type = input("Enter temperature type (C or F): ")
    while temp_type.upper() not in ["C", "F"]:
        temp_type = input("Invalid input. Enter temperature type (C or F): ")
    return temp_type.upper()



# TODO: complete this function which prompt user for the temperature until a valid value is received.
def get_temperature(temperature_type):
    absolute_zero = ABSOLUTE_ZERO_C if temperature_type == "C" else ABSOLUTE_ZERO_F
    temperature = float(input(f"Enter temperature in {temperature_type}: "))
    if temperature < absolute_zero:
        print(f"Temperature cannot be below absolute zero ({absolute_zero}°{temperature_type}).")
        return get_temperature(temperature_type)
    return temperature

# TODO: complete this function which perform conversion based on the type
def display_conversion(temperature_type, temperature):
    if temperature_type == "C":
        converted_temperature = (temperature * 9/5) + 32
        converted_temperature = round(converted_temperature, 2)
        print(f"{temperature}°C is equal to {converted_temperature}°F")
    elif temperature_type == "F":
        converted_temperature = (temperature - 32) * 5/9
        converted_temperature = round(converted_temperature, 2)
        print(f"{temperature}°F is equal to {converted_temperature}°C")
    else:
        print("Invalid temperature type")
    pass


if __name__ == "__main__":
    main()