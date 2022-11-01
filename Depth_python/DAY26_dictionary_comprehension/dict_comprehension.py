# using dict comprehension
# new_dict = {new_key:new_value for item in list}

# Create new_dictionary based on value in existing dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# dictionary with condition
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ['Alex', 'Beth', 'Caroline', 'Syarif', 'Dave', 'Elanor']
students_score = {student: random.randint(1, 100) for student in names}
passed_student = {student: score for (
    student, score) in students_score.items() if score > 60}
print(passed_student)
