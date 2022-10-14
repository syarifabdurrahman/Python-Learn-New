import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
result = []

nr_letter = int(input('how many letter would you like in your password? \n'))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for index_letter in range(nr_letter):
    rand = random.randrange(0,len(letters))
    result.append(letters[rand])

for index_symbol in range(nr_symbols):
    result.append(symbols[rand])

for index_number in range(nr_numbers):
    result.append(numbers[rand])

my_result_str = ''.join(result)

print(my_result_str)