# local vs global

enemies = 1 #this called global scope

def increase_enemies():
    global enemies # with this line, can modifying global scope
    enemies += 2 #this called local scope
    print(f"enemies inside function: {enemies}") 
    # alternative can use return enemy+1 

increase_enemies()
print(f"enemis outside the function: {enemies}")


# if this on the function will be local scope and the print down below will error
books = ["gede","Book"]
game_level =3
if game_level < 5:
    new_book = books[0]

print(new_book) # result is gede

#in python no block scope like if/else/while/

#Global Constants
PI = 3.14159 # this how to define constant
