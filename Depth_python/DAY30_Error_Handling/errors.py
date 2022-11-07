# FileNotFound
# with open("a_file.txt") as file:
#       file.read()

# keyError
# a_dictionary = {'key':'value'}
# value = a_dictionary{'non_existent_key}

# etc

# to block error can use
# try: might cause exception
# except: do this there was an exception
# else: do this where no exception
# finally: do this no matter what happen

# to cause error use raise
height = float(input("Height: "))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Hman height should not be over 3 meters')

bmi = weight/height ** 2
print(bmi)
