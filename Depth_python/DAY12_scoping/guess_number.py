import random
import os

clear = lambda: os.system('cls')

number_choice = random.randint(1,101)
print(number_choice)
attemps = 0
is_start = False

def pick_difficulty(num):
    global attemps
    attemps = num
    return attemps

def any_guess():
    global attemps,is_start
    curr_attemp = attemps
    player_guess = int(input("Make a guess: "))

    if curr_attemp <= 0:
            print(f"Game over! you out of attemps")
            is_start =False
    
    while player_guess != number_choice:
        if player_guess > number_choice:
            print("You Guessed too high!")
            player_guess = int(input("Guess again"))
            curr_attemp -=1
            
        elif player_guess < number_choice:
            print("You guessed too small!")
            player_guess = int(input("Guess again"))
            curr_attemp -=1

    print(f"Congratulations you did it with {attemps} attemps left")


while not is_start :
    difficulty = input("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100 \nChoose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attemps =  pick_difficulty(7)
        print(f"You have {attemps} attemps remaining to gues the number")
    elif difficulty == 'hard':
        attemps = pick_difficulty(5)
        print(f"You have {attemps} attemps remaining to gues the number")

    any_guess()

    play_again = input("You want play again? type 'y' or 'n' : ")

    if play_again == 'y':
        clear()
        is_start = False
        number_choice = random.randint(1,101)
        print(number_choice)
            
    else:
        is_start = True
