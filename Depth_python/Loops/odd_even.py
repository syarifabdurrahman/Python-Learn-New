total_even = 0
total_odd = 0


for number in range(0,100):
    if number % 2 == 0:
        total_even += number
        # print(number)
    else:
        total_odd +=number


print(f"total of even number is {total_even}")
print(f"total of even number is {total_odd}")
