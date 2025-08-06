score = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for student in score:
    student_score = score[student]
    if student_score > 90:
        student_grades[student] = 'Outstanding'
    elif student_score > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif student_score > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
print(student_grades)
    
