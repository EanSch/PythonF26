from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

# Anchor the output files to this script's own folder instead of using bare
# relative filenames, which depends on the working folder where the script gets executed.
SCRIPT_DIR = Path(__file__).resolve().parent
FORLOOP_FILE = SCRIPT_DIR / "temperature_forloop.txt"
WHILELOOP_FILE = SCRIPT_DIR / "temperature_whileloop.txt"


def main():
    celsius = get_celsius()
    write_temperature_file_forloop(celsius)
    write_temperature_file_whileloop(celsius)


def get_celsius():
    celsius = float(input(f"Enter a Celsius value between {MIN_CELSIUS} and {MAX_CELSIUS}: "))
    if celsius <= MIN_CELSIUS or celsius >= MAX_CELSIUS:
        print(f"Invalid input. Please enter a value between {MIN_CELSIUS} and {MAX_CELSIUS}.")
        return get_celsius()
    else:
        return celsius

def write_temperature_file_forloop(celsius):
    #TODO - complete this function to reproduce what below write_temperature_file_whileloop does
    # but using a for-loop
   with open(FORLOOP_FILE, "w") as outfile:
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')
        outfile.write("------------------------------------\n")
        for degree in range(int(celsius) + 1):
            # Calculate C to F
            fahrenheit = (degree * 1.8) + 32
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")


def write_temperature_file_whileloop(celsius):
    with open(WHILELOOP_FILE, "w") as outfile:
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')
        outfile.write("------------------------------------\n")
        degree = 0
        while degree <= celsius:
            # Calculate C to F
            fahrenheit = (degree * 1.8) + 32
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")
            degree += 1


if __name__ == "__main__":
    main()

# Q1: The while loop would be more suitable for this, because I think it makes 
# the computer have one less check to do. In the for loop, it has to check what 
# celsius step its on, where the while loop is a Boolean, so it just has to check 
# for True or False. I think that would be easier on the computer's memory and be 
# more optimized.