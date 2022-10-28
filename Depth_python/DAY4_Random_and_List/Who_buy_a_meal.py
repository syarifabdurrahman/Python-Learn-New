import random

# cara 1
people_name= ['Angela','Ben','Jenny','Michael','Chloe']
random_pay= random.randrange(0,len(people_name))

print(f'{people_name[random_pay]} is going to buy meal today!')

# cara 2
# name_string= input("Give me every body's name, sperate by comma.")
# names=name_string.split(", ") # become a list of names
# print(names)
# random_pay= random.randrange(0,len(names))
# print(f'{names[random_pay]} is going to buy meal today!')

