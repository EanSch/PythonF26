""" Calculate the student's grade based on the score input by 
the user and the weight of the assignment """

# Define the weights of each category
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

# Get the scores from the user
midterm_exam_score = float(input("Enter the midterm exam score (0-100): "))
final_exam_score = float(input("Enter the final exam score (0-100): "))
assignment_one = float(input("Enter the assignment score (0-30): "))
assignment_two = float(input("Enter the second assignment score (0-30): "))
quiz_one = float(input("Enter the first quiz score (0-20): "))
quiz_two = float(input("Enter the second quiz score (0-20): "))


# Test the midterm and final exam grades are within the valid range
if 0 <= midterm_exam_score <= 100 and 0 <= final_exam_score <= 100:
    # Calculate the exam grade
    exam_grade = (midterm_exam_score + final_exam_score) / 2 * EXAM_WEIGHT
else:
    # Print an invalid input for exams
    print("Invalid input for exams. Please enter scores between 0 and 100.")
# Test the assignment grades are within the valid range
if 0 <= assignment_one <= 30 and 0 <= assignment_two <= 30:
    # Calculate the assignment grade
    assignment_grade = (assignment_one + assignment_two) / 60 * 100 * ASSIGNMENT_WEIGHT
else:
    # Print an invalid input for assignments
    print("Invalid input for assignments. Please enter scores between 0 and 30.")
# Test the quiz grades are within the valid range
if 0 <= quiz_one <= 20 and 0 <= quiz_two <= 20:
    # Calculate the quiz grade
    quiz_grade = (quiz_one + quiz_two) / 40 * 100 * QUIZ_WEIGHT
else:
    # Print an invalid input for quizzes
    print("Invalid input for quizzes. Please enter scores between 0 and 20.")
# Add the final grade
if (0 <= midterm_exam_score <= 100 and 0 <= final_exam_score <= 100) and (0 <= assignment_one <= 30 and 0 <= assignment_two <= 30) and (0 <= quiz_one <= 20 and 0 <= quiz_two <= 20):
    print(f"The student's final grade is: {exam_grade + assignment_grade + quiz_grade:.2f}")
else:
    print("Cannot calculate final grade due to invalid input.")