from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent / "grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, calculate weighted grades, and print a summary."""

    try:
        weight_final_list = []

        with open(GRADES_FILE, "r") as file:
            next(file)  # Skip header row

            for line in file:
                row = line.strip().split(",")

                if row:
                    grade = process_row(row)
                    weight_final_list.append(grade)

        analyze_grade(weight_final_list)

    except FileNotFoundError:
        print("Error: Grades file could not be found.")

    except Exception as error:
        print("An error occurred:", error)


def process_row(row):
    """Calculate one student's weighted final grade."""

    test_avg = average_subject(row[2:6])
    exam_avg = average_subject(row[6:8])
    discussion_avg = average_subject(row[8:10])
    project_score = float(row[10])

    return weight_final(test_avg, exam_avg, discussion_avg, project_score)


def average_subject(subject_list):
    """Return the average of the scores in subject_list."""

    total = 0

    for score in subject_list:
        total += float(score)

    return total / len(subject_list)


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Calculate the weighted final grade."""

    final_grade = (
        test_avg * TEST_WEIGHT
        + exam_avg * EXAM_WEIGHT
        + discussion_avg * DISCUSSION_WEIGHT
        + project_score * PROJECT_WEIGHT
    )

    return final_grade


def analyze_grade(weight_final_list):
    """Count students in each final grade range."""

    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0

    for grade in weight_final_list:
        if grade >= 90:
            a_count += 1
        elif grade >= 80:
            b_count += 1
        elif grade >= 70:
            c_count += 1
        elif grade >= 60:
            d_count += 1
        else:
            f_count += 1

    print("\nGrade Summary")
    print("90 or above:", a_count)
    print("80-89:", b_count)
    print("70-79:", c_count)
    print("60-69:", d_count)
    print("Below 60:", f_count)


if __name__ == "__main__":
    main()
