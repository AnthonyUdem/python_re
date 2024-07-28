#Step 4
import random
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
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1.
#If lives goes down to 0 then the game should stop and it should print "You lose."
#Join all the elements in the list and turn it into a String.
# print(f"{' '.join(display)}")
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of
# 'lives' the user has remaining.


def check_live_track():
    """Checks the track of user's live and print the ASCII art as follows"""

    word_list = ["pancake", "banana", "cornflakes", "apple", "swimming", "watermelon", "gymnastics", "love", "ice"]
    # word_list = ["apple"]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 6   # todo-1

    # Create blanks
    display = []
    for word in range(word_length):
        display += "-"

    #while loop check if user has completely guessing the chosen word
    end_of_game = False
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Keeping track of user's lif
        if guess not in chosen_word:    # todo-2
            lives -= 1
            print(stages[lives])        # todo-3
        print(" ".join(display))

        # Check if user has got all letters.
        if '-' not in display:
            end_of_game = True
            print("Congrats!😃 you've won🏆")
        elif lives == 0:                # todo-2
            end_of_game = True
            print("You lose😞 Game Over!")


check_live_track()