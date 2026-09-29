# Input an integer the program should convert up to
celsius = int(input("Enter a Celsius degree: "))

# Check for absolute zero
absolute_zero = -273.15
if celsius < absolute_zero:
    print("Error: Temperature cannot be below absolute zero.")

# Print the conversion table
print("Celsius\tFahrenheit")
print("-------------------------")
for i in range(celsius + 1):
    fahrenheit = (i * 9/5) + 32
    print(f"{i}\t{fahrenheit}")
