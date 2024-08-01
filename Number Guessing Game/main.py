# -------------------------------Method 2 ---------------------------------#
# Todo-1 print a welcome message to the user and the logo
#          tell them you're thinking of a number between 1 and 100
#          ask them to chose a difficulty level: easy or hard.
# Todo-2 they have 10 attempt for easy, 5 for hard to guess the number.
#         ask them to make a guess.
# Todo-3 print too high or too low depending on their guess close to the number and ask them to guess again
#         display their current chances while they guess wrong.
#         repeat todo 2 and 3 to keep asking for a guess until they guessed correctly
#
# todo-4 if they got the number or not, print the number and say they've won or lost

import random
from art import logo

print(logo)

# creating a random number between 1 and 100#
# def number_List():
#     """create a list of numbers between 1 and 100"""
#     numbers = []
#     for num in range(1, 101):
#         numbers.append(num)
#     return numbers
# guessed_number = random.choice(number_List())
guessed_number = random.randint(1, 100)

print("Welcome to The Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty level. Type 'e' for easy or 'h' for hard: ")


def play():
    global number_of_attempt
    still_guessing = True
    while still_guessing:
        if number_of_attempt > 1:
            print(f"you have {number_of_attempt} attempts remaining to guess the number")
        else:
            print(f"This is your last chance!🙃")
        user_guess = int(input("make a guess: "))

        if user_guess == guessed_number:
            still_guessing = False
            print(f"  Correct!😃 you got it, the answer was {guessed_number}")
        elif number_of_attempt == 1:
            still_guessing = False
            print(f"You have exhausted your chances. The number was: {guessed_number}\nGame Over!😤")
        elif user_guess < guessed_number:
            number_of_attempt -= 1
            print(f"  {user_guess} is too low.\n  Guess again😎.")
        elif user_guess > guessed_number:
            number_of_attempt -= 1
            print(f"  {user_guess} is too high.\n  Guess again😎.")


if difficulty == 'e':
    number_of_attempt = 10
    play()
elif difficulty == 'h':
    number_of_attempt = 5
    play()
else:
    print("you entered a wrong letter!")

# -------------------------------Method 2 end -------------------------------#

# #-------------------------------Method 1 ---------------------------------#
#
# from random import randint
# from art import logo
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
#
# # Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#     """checks answer against guess. Returns the number of turns remaining."""
#     if guess > answer:
#         print("Too high.")
#         return turns - 1
#     elif guess < answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {answer}.")
#
#
# # Make function to set difficulty.
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
#
#
# def game():
#     print(logo)
#     # Choosing a random number between 1 and 100.
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(1, 100)
#     print(f"Pssst, the correct answer is {answer}")
#
#     turns = set_difficulty()
#     # Repeat the guessing functionality if they get it wrong.
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#
#         # Let the user guess a number.
#         guess = int(input("Make a guess: "))
#
#         # Track the number of turns and reduce by 1 if they get it wrong.
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")
#
#
# game()

# #------------------------------- Method 1 end ---------------------------#
