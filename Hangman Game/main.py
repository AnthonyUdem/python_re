import random
from hangman_words import word_list
from hangman_art import logo, stages


# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# TODO-2: - Import the stages from hangman_art.py and make this error go away.

def hangman_game():
    """Ask the user to predict a random word chosen by the computer and displays the live track"""

    print("Welcome to the hangman game!\nThis program is about predicting a random word chosen by the computer.")
    chosen_word = random.choice(word_list)  # todo-1
    print(logo)  # todo-3
    # print(chosen_word)
    word_length = len(chosen_word)
    lives = 6

    # Create blanks
    display = []
    for word in range(word_length):
        display += "-"

    # while loop check if user has completely guessing the chosen word
    end_of_game = False
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # checking if user's guess already exist
        if guess in display:  # todo-4
            print(f"you've already guessed '{guess}'")

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong
        if guess not in chosen_word:
            lives -= 1
            if lives > 1:  # todo-5
                print(f"'{guess}' is not in the word; you lose a life! you have '{lives}' chances remaining")
            if lives == 1:
                print(f"'{guess}' is not in the word; you lose a life! you have '{lives}' chance remaining")
            print(stages[lives])  # todo-2
            if lives == 0:
                end_of_game = True
                print("You lose😞 Game Over!")

        # Join all the elements in the list and turn it into a String.
        print(" ".join(display))

        # Check if user has got all letters.
        if '-' not in display:
            end_of_game = True
            print("Congrats!😃 you've won🏆")

    print(f"This is the required word: {chosen_word} 😃")


hangman_game()
