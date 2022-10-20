# def my_function(something):
#     #Do this with something
#     #Then do this
#     #Finally do this

# def my_function():
#     result = 3 * 2
#     return result

# def format_name(f_name,l_name):
#     result =f"{f_name.title()} {l_name.title()}"
#     return result

# print(format_name('SYArif','AbdurraHman'))


#returning multiple values
def format_name(f_name,l_name):
    """
    Take a first and last name and format it
    to return title case version 
    """
    if f_name == ""or l_name == "":
        return

    result =f"{f_name.title()} {l_name.title()}"
    return result

f_input = input("What is your first name? ")
l_input = input("What is your last name? ")

print(format_name(f_input,l_input))
