student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

print(student_grades)
for score in student_scores:
    if student_scores[score] >= 91:
        student_grades[score] = "Outstanding"
        print(student_grades)
    elif student_scores[score] >= 81 and student_scores[score] <= 90:
        student_grades[score] = "Exceeds Expectations"
        print(student_grades)
    elif student_scores[score] >= 71 and student_scores[score] <= 80:
        student_grades[score] = "Acceptable"
        print(student_grades)
    elif student_scores[score] <= 70:
        student_grades[score] = "Fail"
        print(student_grades)