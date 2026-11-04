from pathlib import Path


def main():
    filename = input("Enter the name of the input file: ")

    word_count = {}

    try:
        file_path = Path(__file__).resolve().parent / filename

        with open(file_path, "r") as file:
            text = file.read()

            words = text.split()

            unique_words = set(words)

            for word in unique_words:
                word_count[word] = words.count(word)

        print("\nWord                Occurrences")
        print("----------------------------------------")

        for word, count in word_count.items():
            print(f"{word:<20}{count}")

    except FileNotFoundError:
        print("Error: File could not be found.")

    except Exception as error:
        print("An error occurred:", error)


if __name__ == "__main__":
    main()