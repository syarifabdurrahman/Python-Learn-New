student_scores ={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}

student_grade = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grade[key] = "Outstanding"
    elif student_scores[key] >80 and student_scores[key] <= 90:
        student_grade[key] = "Exceeds Expectation"
    else:
        student_grade[key] = "Acceptable"
    
    print(f"{key} grade: {student_grade[key]}")

