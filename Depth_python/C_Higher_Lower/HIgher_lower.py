import random
from game_data import data
from art import logo,vs
import os

clear = lambda: os.system('cls')

def randomize_data(data):
    return random.choice(data)

score = 0
is_playing = False

def get_spesific_data(result_data):
    name = result_data['name']
    description = result_data['description']
    country = result_data['country']
    return f"{name}, a {description}, from {country}"

def checking_High_Low():
    global score, is_playing,result_data_A,result_data_B

    print("\033[H\033[J", end="")
    print(logo)
    if score == 0:
        print(f'compare A: {get_spesific_data(result_data_A)}')
        print(vs)
        print(f'Againts B: {get_spesific_data(result_data_B)}')
    else:
        print(f'You\'re right! current score: {score}')
        print(f'compare A: {get_spesific_data(result_data_A)}')
        print(vs)
        print(f'Againts B: {get_spesific_data(result_data_B)}')

    is_more = input('Who has more followers? Type "A" or "B": ').lower()
    if is_more == 'a' and result_data_A['follower_count'] > result_data_B['follower_count']:
        score += 1
        result_data_A = randomize_data(data)
        result_data_B = randomize_data(data)
        checking_High_Low()
    elif is_more == 'a' and result_data_A['follower_count'] < result_data_B['follower_count']:
        clear()
        print(f"Sorry, that\'s wrong. Final score: {score}")
        is_play_again = input("Want play again? Type 'y' or 'n': ")
        if is_play_again == 'y':
            score = 0
            is_playing = True
        else:
            is_playing = False # probably error

    if is_more == 'b' and result_data_B['follower_count'] > result_data_A['follower_count']:
        score += 1
        result_data_A = randomize_data(data)
        result_data_B = randomize_data(data)
        checking_High_Low()
    elif is_more == 'b' and result_data_B['follower_count'] < result_data_A['follower_count']:
        clear()
        print(f"Sorry, that\'s wrong. Final score: {score}")
        is_play_again = input("Want play again? Type 'y' or 'n': ")
        if is_play_again == 'y':
            score = 0
            is_playing = True
        else:
            is_playing = False # probably error

if __name__ == "__main__":
    is_playing = True
    print(logo)

    while is_playing:
        result_data_A = randomize_data(data)
        result_data_B = randomize_data(data)

        while  result_data_A ==  result_data_B:
            result_data_B = randomize_data(data)

        checking_High_Low()