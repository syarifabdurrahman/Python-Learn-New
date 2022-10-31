numbers = [1, 2, 3]
name = "Syarif"

# For loop that we usually used
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# using list comprehension
# new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]
print(new_list)
new_list = [letter for letter in name]
print(new_list)
new_list = [n*2 for n in range(1, 5)]
print(new_list)

# using Conditional list comprehension
# new_list = [new_item for item in list if test]
names = ['Alex', 'Beth', 'Caroline', 'Syarif', 'Dave', 'Elanor']
new_list_name = [name.upper() for name in names if len(name) > 5]
print(new_list_name)
