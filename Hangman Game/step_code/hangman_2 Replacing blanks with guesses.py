#Step 2
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each
# letter to guess.
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter
# replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
import random


def blank_guess():
    """Ask for a letter and check if it matches with the random chosen word then place the letter in position"""

    print("This program will check if your letter matches with the random chosen word, then, "
          "place the letter in the exact position")
    word_list = ["pancake", "banana", "cornflakes", "apple", "swimming", "watermelon", "gymnastics", "love"]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    # Create blanks
    display = []
    for word in range(word_length):
        display += "-"

    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    print(chosen_word)


blank_guess()