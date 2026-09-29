""" Calculate the student's grade based on the score input by 
the user and the weight of the assignment """

# Define the weights of each category
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

# Get the scores from the user
midterm_exam_score = float(input("Enter the midterm exam score (0-100): "))
final_exam_score = float(input("Enter the final exam score (0-100): "))
assignment_one = float(input("Enter the assignment score (0-100): "))
assignment_two = float(input("Enter the second assignment score (0-100): "))
quiz_one = float(input("Enter the first quiz score (0-100): "))
quiz_two = float(input("Enter the second quiz score (0-100): "))

# Calculate the weighted scores
exam_grade = (midterm_exam_score + final_exam_score) / 2 * EXAM_WEIGHT
assignment_grade = (assignment_one + assignment_two) / 2 * ASSIGNMENT_WEIGHT
quiz_grade = (quiz_one + quiz_two) / 2 * QUIZ_WEIGHT

#print the final grade
print(f"The student's final grade is: {exam_grade + assignment_grade + quiz_grade:.2f}")