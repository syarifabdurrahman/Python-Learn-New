
# students_heights=[180,124,165,173,189,146,169]
# result =0 

# for n in range(0,len(students_heights)):
#     result = result + students_heights[n]
#     average_value= result/len(students_heights)

# print(round(average_value))

student_heights= input('Type the student\'s heights: \n').split()
print(student_heights)

result=0

for n in range(0,len(student_heights)):
    result += int(student_heights[n])
    average_value = result/len(student_heights)

print(result)
print(round(average_value))