import random

# display.clear()
    
word_list = ["cat","camel","baboon","mouse"]
word_index_rand = random.randrange(len(word_list))
chosen_word = word_list[word_index_rand]
print(chosen_word)
game_over = False
display = []
current_live = 6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


def displaying_word(display_word):
    for index in range(len(chosen_word)):
         display_word+="_"
    print(f"player has {current_live} health\'s")
    

if __name__ == "__main__":
    displaying_word(display)
    while game_over == False:
        guess = input ("guess a letter: ").lower()

        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess

        print(display)

        if guess not in chosen_word:
            current_live -= 1
            if current_live == 0:
                game_over = True
                print("You lose.")

        print(stages[current_live])
        print(f"player has {current_live} health\'s")

        if "_" not in display:
            game_over = True
            print("You win")
            

