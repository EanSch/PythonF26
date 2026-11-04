import random


def main():
    states = {
        "Illinois": "Springfield",
        "California": "Sacramento",
        "Texas": "Austin",
        "Florida": "Tallahassee",
        "New York": "Albany",
        "Ohio": "Columbus",
        "Michigan": "Lansing",
        "Georgia": "Atlanta",
        "Colorado": "Denver",
        "Arizona": "Phoenix",
        "Wisconsin": "Madison",
        "Oregon": "Salem"
    }

    correct = 0
    incorrect = 0

    print("Welcome to the State Capitals Game!")
    print("Enter '0' to end the game.\n")

    while True:
        state = random.choice(list(states.keys()))

        answer = input("What is the capital of " + state + "? ")

        if answer.lower() == "0":
            break

        if answer.lower() == states[state].lower():
            print("That is correct!")
            correct += 1
        else:
            print("That is incorrect.\n")
            incorrect += 1


    print("You had", correct, "correct responses and", incorrect, "incorrect responses.")


if __name__ == "__main__":
    main()