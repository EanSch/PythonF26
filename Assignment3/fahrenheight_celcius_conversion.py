# Input the unit of the temperature
temp = float(input("Enter the temperature you want to convert: "))
unit = input("Enter the unit of the temperature (F for Fahrenheit, C for Celsius): ")

# Test the temperature type is F
if unit == 'F':
    # Test the temperature is above absolute zero
    if temp >= -459.67:
        # Convert Fahrenheit to Celsius
        converted_temp = (temp - 32) * 5/9
        print("The temperature in Celsius is:", converted_temp)
    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")
elif unit == 'C':
    # Test the temperature is above absolute zero
    if temp >= -273.15:
        # Convert Celsius to Fahrenheit
        converted_temp = (temp * 9/5) + 32
        print("The temperature in Fahrenheit is:", converted_temp)
    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")
else:
    print("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")