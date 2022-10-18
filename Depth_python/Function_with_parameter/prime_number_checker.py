test_num = int(input('Enter the number: '))


def check_number(number):
    if number <= 1:
        print("The prime number has greater than 1")

    if number % 2 == 0 or number % 3 == 0:
        if number == 2 or number == 3:
            print(f"Yes, this {number} is Prime number")
        else:
            print(f"No, this {number} is not Prime number")
    else:
        print(f"Yes, this {number} is Prime number")
        
check_number(number= test_num)