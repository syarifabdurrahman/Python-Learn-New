import os

clear = lambda: os.system('cls')

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")
    return result
 
def subtract(n1, n2):
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")
    return result
 
def multiply(n1, n2):
    result = n1 * n2
    print(f"{n1} * {n2} = {result}")
    return result
 
def divide(n1, n2):
    result = n1 / n2
    print(f"{n1} / {n2} = {result}")
    return result

def check_operation(operation_symbol,first_num,next_num,result):
    if operation_symbol == "+":
        result = add(first_num,next_num)
        return result
    elif operation_symbol == "-":
        result = subtract(first_num,next_num)
        return result
    elif operation_symbol == "*":
        result = multiply(first_num,next_num)
        return result
    elif operation_symbol == "/":
        result = divide(first_num,next_num)
        return result
    else:
        print("errot there is no symbol like that!")

def start():
    print(logo)
    result = 0
    operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
        }
    first_num = int(input("What\'s the first number?"))
    for operation in operations:
        print(operation)
    operation_symbol= input("Pick an operation from the line above : ")
    next_num = int(input("What\'s the next number?"))
    result = check_operation(operation_symbol=operation_symbol,first_num=first_num,next_num=next_num,result=result)
    is_continue= input(f"Type 'y' to continue calculating with {result}, or type 'n to start a new calculation:")
    if is_continue == 'y':
        first_num = result
        for operation in operations:
            print(operation)
        operation_symbol= input("Pick an operation from the line above : ")
        next_num = int(input("What\'s the next number?"))
        check_operation(operation_symbol=operation_symbol,first_num=first_num,next_num=next_num,result=result)
    elif is_continue == 'n':
        clear()
        start()
    else:
        print("Wrong input!")

start()
