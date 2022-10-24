# rule 
# score must less than 21 if greater bust: lose
# J,K,Q = 10 
# A = 1 or 11 depend
# if score less than 17  take another card

import random
import os

clear = lambda: os.system('cls')

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

is_play = True
card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards = []
computer_cards = []
player_score = 0
computer_score = 0

def deal_card(picked,get_card):
    for index in range(get_card):
        card_picked = random.choice(card_list)
        picked.append(card_picked)

def add_total(total_card):
    return sum(total_card)

def take_card(player_cards,user_score):
    if is_another =='y':
        deal_card(player_cards,1)
        if user_score > 21 and 11 in player_cards:
            player_cards.remove(11)
            player_cards.append(1)
        user_score = add_total(player_cards)
        print(f"    Your cards: {player_cards}, current score: {user_score}")
        return False
    else:
        return True

def check_score(player_score,computer_score):
    if player_score > 21:
        print("     Player bust!")
    if computer_score > 21:
        print("     Computer bust!")

    if player_score > computer_score and player_score <= 21:
        print("     You win!")
    elif player_score < computer_score and computer_score <= 21:
        print("     You lose!")
    elif player_score > computer_score:
        print("     You lose!")
    elif player_score < computer_score:
        print("     You win!")
    elif player_score == computer_score:
        print("     Draw!")
    

if __name__ == '__main__':
    exit_check = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")
    if exit == 'y':
        is_play = False
    else:
        is_play = True

    while is_play:
        print(logo)

        is_finished = False

        deal_card(player_cards,2)
        deal_card(computer_cards,2)
        player_score = add_total(player_cards)

        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        while not is_finished:
            is_another = input("Type 'y' to get another card, type 'n' to pass: ")
            is_finished = take_card(player_cards,player_score)

        computer_score = add_total(computer_cards)
        player_score = add_total(player_cards)

        #giving computer card
        while computer_score < 17:
            deal_card(computer_cards,1)
            computer_score = add_total(computer_cards)

        # Who is the winner check
        print(f"    Your final hand: {player_cards}, final score: {player_score}")
        print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

        check_score(player_score,computer_score)
        exit_check = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")
        if exit == 'y':
            clear()
            is_play = True
        else:
            is_play = False





