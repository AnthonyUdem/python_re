# ----------------------------- Methode 1 request to play again ----------------------
game_is_on = True
while game_is_on:
    def blackjack_game():
        import random
        from art import logo
        print("Welcome to The Lonasctech Blackjack 21 Game.")
        print(logo)

        # The user and computer should each get two random cards#
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = random.sample(cards, 2)
        comp_cards = random.sample(cards, 2)

        def comp_blackjack():
            if 10 in comp_cards and 11 in comp_cards:
                return True

        def user_blackjack():
            if 10 in user_cards and 11 in user_cards:
                return True

        # Add up the user and computer's scores#
        def comp_score():
            sum_comp = 0
            for num in comp_cards:
                sum_comp += num
            return sum_comp

        def user_score():
            sum_user = 0
            for num in user_cards:
                sum_user += num
            return sum_user

        def print_user_win():
            global game_is_on
            print(f"  Your final hand: {user_cards}, final score: {user_score()}")
            print(f"  Computer's final hand: {comp_cards}, final score: {comp_score()}")
            print("  You win!😁")
            game_is_on = False

        def print_draw():
            global game_is_on
            print(f"  Your final hand: {user_cards}, final score: {user_score()}")
            print(f"  Computer's final hand: {comp_cards}, final score: {comp_score()}")
            print("  It's a draw🙃")
            game_is_on = False

        def print_user_lose():
            global game_is_on
            print(f"  Your final hand: {user_cards}, final score: {user_score()}")
            print(f"  Computer's final hand: {comp_cards}, final score: {comp_score()}")
            print("  You lose!😤")
            game_is_on = False

        # is an ace drawn?#
        def is_an_ace_drawn():
            if 11 in user_cards:
                return True

        def to_pass():
            # Computer plays, if score is less than 17, keep drawing cards#
            while comp_score() < 17:
                comp_cards.append(random.choice(cards))
            # Has computer gone over 21#
            if comp_score() > 21:
                # Yes, WIN#
                print("  Computer went over!😃")
                print_user_win()
            # Compare user score with computer score to see if user score is higher?#
            elif user_score() > comp_score():
                # User score higher, WIN#
                print("  You score higher!😃")
                print_user_win()
            elif user_score() == comp_score():
                # Same score, DRAW#
                print("  You both have same score!")
                print_draw()
            else:
                # User score lower, LOSE#
                print("  Computer has a higher score!😭")
                print_user_lose()

        def wants_another_card():
            # Ask the user if they want to get another card#
            another_card = input("Type 'y' to get another card, type 'p' to pass: ").lower()
            if another_card == 'y':
                # Draw another card#
                user_cards.append(random.choice(cards))
                if not is_an_ace_drawn():
                    print(f"  Your cards: {user_cards}, current score: {user_score()}")
                above_21()
            elif another_card == 'p':
                to_pass()

        def above_21():
            global game_is_on
            # if an ace is drawn#
            if is_an_ace_drawn():
                # Is the user score over 21#
                if user_score() > 21:
                    user_cards.remove(11)
                    user_cards.append(1)
                    # If the ace counts as a 1 instead of 11, are they still over 21?#
                    if user_score() > 21:
                        # Yes, LOSE#        #score is still above 21
                        print("  You went over!😭")
                        print_user_lose()
                    else:
                        # if score is not above 21
                        wants_another_card()
                else:
                    # score is less than 21
                    wants_another_card()

            elif user_score() > 21:
                # ace wasn't drawn
                print("  You went over!😭")
                print_user_lose()
            else:
                # score is less than 21 and ace wasn't drawn
                wants_another_card()

        def check_blackjack():
            # Does the user or computer have a blackjack (ace + 10)?#
            if comp_blackjack() and user_blackjack():
                # It's a draw#
                print("  You both have a blackjack😎")
                print_draw()
            elif comp_blackjack():
                # Computer wins#
                print("  Computer has a blackjack😎")
                print_user_lose()
            elif user_blackjack():
                # User wins#
                print("  A blackjack😎")
                print_user_win()

        # Print user's cards and computer's first card#
        print(f"  Your cards: {user_cards}, current score: {user_score()}")
        print(f"  Computer's first card: {comp_cards[0]}")

        # calling functions#
        check_blackjack()
        if not comp_blackjack() and not user_blackjack():
            above_21()


    to_continue = True
    while to_continue:
        again = input("Do you want to play a game of blackjack? Type 'y' for yes or 'n' for no: ").lower()
        if again == 'y':
            blackjack_game()
        else:
            to_continue = False
            print("  Goodbye!")

# ----------------------------- Methode 1 end -----------------------------------------


# ----------------------------- Methode 2 no request to play again ---------------------
# again = input("Do you want to play a game of blackjack? Type 'y' for yes or 'n' for no: ").lower()
# if again == 'y':
#     print("Welcome to The Lonasctech Blackjack 21 Game.")
#     import random
#     from art import logo
#     print(logo)
#
#     # The user and computer should each get two random cards#
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     user_cards = random.sample(cards, 2)
#     comp_cards = random.sample(cards, 2)
#
#     # comp_cards = [10, 11]
#
#     def comp_blackjack():
#         if 10 in comp_cards and 11 in comp_cards:
#             return True
#
#     def user_blackjack():
#         if 10 in user_cards and 11 in user_cards:
#             return True
#
#     # Add up the user and computer's scores#
#     def comp_score():
#         sum_comp = 0
#         for num in comp_cards:
#             sum_comp += num
#         return sum_comp
#
#     def user_score():
#         sum_user = 0
#         for num in user_cards:
#             sum_user += num
#         return sum_user
#
#     def print_user_win():
#         global game_is_on
#         print(f"  Your final hand: {user_cards}, final score: {user_score()}")
#         print(f"  Computer's final hand: {comp_cards}, final score: {comp_score()}")
#         print("  You win!😁")
#         game_is_on = False
#
#     def print_draw():
#         global game_is_on
#         print(f"  Your final hand: {user_cards}, final score: {user_score()}")
#         print(f"  Computer's final hand: {comp_cards}, final score: {comp_score()}")
#         print("  It's a draw🙃")
#         game_is_on = False
#
#     def print_user_lose():
#         global game_is_on
#         print(f"  Your final hand: {user_cards}, final score: {user_score()}")
#         print(f"  Computer's final hand: {comp_cards}, final score: {comp_score()}")
#         print("You lose!😤")
#         game_is_on = False
#
#     # is an ace drawn?#
#     def is_an_ace_drawn():
#         if 11 in user_cards:
#             return True
#
#     def to_pass():
#         # Computer plays, if score is less than 17, keep drawing cards#
#         while comp_score() < 17:
#             comp_cards.append(random.choice(cards))
#         # Has computer gone over 21#
#         if comp_score() > 21:
#             # Yes, WIN#
#             print("  Computer went over!😃")
#             print_user_win()
#         # Compare user score with computer score to see if user score is higher?#
#         elif user_score() > comp_score():
#             # User score higher, WIN#
#             print("  You score higher!😃")
#             print_user_win()
#         elif user_score() == comp_score():
#             # Same score, DRAW#
#             print("  You both have same score!")
#             print_draw()
#         else:
#             # User score lower, LOSE#
#             print("  Computer has a higher score!😭")
#             print_user_lose()
#
#     def wants_another_card():
#         # Ask the user if they want to get another card#
#         another_card = input("Type 'y' to get another card, type 'p' to pass: ").lower()
#         if another_card == 'y':
#             # Draw another card#
#             user_cards.append(random.choice(cards))
#             if not is_an_ace_drawn():
#                 print(f"Your cards: {user_cards}, current score: {user_score()}")
#             above_21()
#         elif another_card == 'p':
#             to_pass()
#
#     def above_21():
#         global game_is_on
#         # if an ace is drawn#
#         if is_an_ace_drawn():
#             # Is the user score over 21#
#             if user_score() > 21:
#                 user_cards.remove(11)
#                 user_cards.append(1)
#                 # If the ace counts as a 1 instead of 11, are they still over 21?#
#                 if user_score() > 21:
#                     # Yes, LOSE#        #score is still above 21
#                     print("  You went over!😭")
#                     print_user_lose()
#                 else:
#                     # if score is not above 21
#                     wants_another_card()
#             else:
#                 # score is less than 21
#                 wants_another_card()
#
#         elif user_score() > 21:
#             # ace wasn't drawn
#             print("  You went over!😭")
#             print_user_lose()
#         else:
#             # score is less than 21 and ace wasn't drawn
#             wants_another_card()
#
#     def check_blackjack():
#         # Does the user or computer have a blackjack (ace + 10)?#
#         if comp_blackjack() and user_blackjack():
#             # It's a draw#
#             print("  You both have a blackjack😎")
#             print_draw()
#         elif comp_blackjack():
#             # Computer wins#
#             print("  Computer has a blackjack😎")
#             print_user_lose()
#         elif user_blackjack():
#             # User wins#
#             print("  A blackjack😎")
#             print_user_win()
#
#     # Print user's cards and computer's first card#
#     print(f"  Your cards: {user_cards}, current score: {user_score()}")
#     print(f"  Computer's first card: {comp_cards[0]}")
#
#     game_is_on = True
#     while game_is_on:
#         def blackjack_game():
#             check_blackjack()
#             if not comp_blackjack() and not user_blackjack():
#                 above_21()
#
#         blackjack_game()
#
# elif again == 'n':
#     print("Good bye!")

# ----------------------------- Methode 2 end -----------------------------------------
