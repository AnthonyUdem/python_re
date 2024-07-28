# Step 3
# TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters
# in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.
import random


def complete_guess():
    """Runs till user guesses all the letters in the word"""
    word_list = ["pancake", "banana", "cornflakes", "apple", "swimming", "watermelon", "gymnastics", "love", "ice"]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    # Create blanks
    display = []
    for word in range(word_length):
        display += "-"

    #while loop check if user has completely guessing the chosen word
    end_of_game = False
    while not end_of_game:      # todo-1
        guess = input("Guess a letter: ").lower()

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(display)

        # Check if user has got all letters.
        if '-' not in display:
            end_of_game = True
            print("Congrats!😃 you've won🏆")


complete_guess()