import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# looping through data frame:
# for (key, value) in student_data_frame.items():
#     print(key)

# looping through row of data frame:
# for (index, row) in student_data_frame.iterrows():
#     print(row.score)

# using dict comprehension
# {new_key: new_valeu for (index, row) in df.iterrows()}
