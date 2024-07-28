#Step 1
#TODO-1 - randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen word.
import random


def random_word():
    """Ask for a letter and check if it matches with the random chosen word"""

    print("This program would check if the letter you input matched the chosen word.")
    word_list = ["pancake", "banana", "cornflakes", "Apple"]
    chosen_word = random.choice(word_list)  # todo-1
    guess = input("Guess a letter: ").lower()   # todo-2
    for char in chosen_word:    # todo-3
        if char == guess:
            print("Right")
        else:
            print("Wrong")

    print(f"The word is: {chosen_word}")


random_word()