from art import logo, vs
from game_data import data
import random

print(logo)
compareA = random.choice(data)
compareB = random.choice(data)
follower_countA = compareA["follower_count"]
follower_countB = compareB["follower_count"]


def detailsA():
    details = f"{compareA["name"]}, a {compareA["description"]}, from {compareA["country"]}."
    return details


def detailsB():
    details = f"{compareB["name"]}, a {compareB["description"]}, from {compareB["country"]}."
    return details


account_a = detailsA()
account_b = detailsB()
score = 0


def result(comp1, comp2, ans):
    global keep_playing, score
    if comp1 > comp2 and ans == "A":
        score += 1
        return f"  You're right!😃  Current score: {score} 👏"
    elif comp2 > comp1 and ans == "B":
        score += 1
        return f"  You're right!😃  Current score: {score} 👏"
    elif comp1 == comp2:
        return "  That's a tie!😎  Please continue."
    else:
        keep_playing = False
        return f"  Sorry, that's wrong!😤  A:{comp1}  B:{comp2}  Final score: {score}\nGame Over!"


keep_playing = True
while keep_playing:
    compareC = random.choice(data)


    def detailsC():
        details = f"{compareC["name"]}, a {compareC["description"]}, from {compareC["country"]}."
        return details


    follower_countC = compareC["follower_count"]
    account_c = detailsC()

    print(f"Compare A: {account_a}")
    print(vs)
    print(f"Against B: {account_b}")
    answer = input("  Who has more followers on instagram? Type 'A' or 'B': ").upper()
    print(logo)
    print(result(follower_countA, follower_countB, answer))

    account_a = account_b
    account_b = account_c
    follower_countA = follower_countB
    follower_countB = follower_countC

# ----------------------------- Method 2 end ----------------------------------------#

# ----------------------------- Method 1 ---------------------------------------------#
# from game_data import data
# import random
# from art import logo, vs
#
# def get_random_account():
#     """Get data from random account"""
#     return random.choice(data)
#
#
# def format_data(account):
#     """Format account into printable format: name, description and country"""
#     name = account["name"]
#     description = account["description"]
#     country = account["country"]
#     # print(f'{name}: {account["follower_count"]}')
#     return f"{name}, a {description}, from {country}"
#
#
# def check_answer(guess, a_followers, b_followers):
#     """Checks followers against user's guess
#     and returns True if they got it right.
#     Or False if they got it wrong."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# def game():
#     print(logo)
#     score = 0
#     game_should_continue = True
#     account_a = get_random_account()
#     account_b = get_random_account()
#
#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()
#
#         while account_a == account_b:
#             account_b = get_random_account()
#
#         print(f"Compare A: {format_data(account_a)}.")
#         print(vs)
#         print(f"Against B: {format_data(account_b)}.")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#         a_follower_count = account_a["follower_count"]
#         b_follower_count = account_b["follower_count"]
#         is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#         print(logo)
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}.")
#         else:
#             game_should_continue = False
#             print(f"Sorry, that's wrong. Final score: {score}")
#
#
# game()

# ----------------------------- Method 1 end ----------------------------------------#
