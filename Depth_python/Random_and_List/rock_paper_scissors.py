import random

objetive = ['Rock', 'Paper' ,'Scissors']

player = int( input(f'what do you choose?  0 for {objetive[0]}, 1 for {objetive[1]}, 2 for {objetive[2]} \n'))
computer = random.randrange(0,len(objetive))
print(f'Player choose: {objetive[player]}')
print(f'computer choose: {objetive[computer]} \n')

if player == computer:
    print('Draw')

elif player == 0 and computer == 1:
    print('Computer win!')
elif player == 1 and computer == 0:
    print('Player win!')

elif player == 0 and computer == 2:
    print('Player win!')
elif player == 2 and computer == 0:
    print('Computer win!')

elif player == 2 and computer == 1:
    print('Player win!')
elif player == 1 and computer == 2:
    print('Computer win!')

