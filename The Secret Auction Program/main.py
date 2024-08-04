# ---------------------- Method 1 -----------------------------
def secret_auction_game():
    from art import logo
    print(logo)
    print("Welcome to The Lonasctech Secret Auction Program\n")
    players = {}

    def find_highest_bidder(bidding_record):
        highest_bid = 0
        highest_bidder = ""
        for bidder in bidding_record:
            bid_amount = bidding_record[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                highest_bidder = bidder
        print(f"The winner is {highest_bidder} with the highest bid of ${highest_bid}")

    more_bid = True
    while more_bid:
        name = input("What is your name?: ").title()
        bid = int(input("What's your bid?: $"))
        players[name] = bid
        other_bids = input("Are there any other bidders? Type y for 'yes' or n for 'no': ")
        if other_bids == 'n':
            more_bid = False
            print("-------------------------------------------")
            find_highest_bidder(bidding_record=players)


secret_auction_game()
# ---------------------- Method 1 end -----------------------------

# ---------------------- Method 2 ---------------------------------
# def secret_auction_game():
#     from art import logo
#     print(logo)
#     print("Welcome to The Lonasctech Secret Auction Program\n")
#     player_list = []
#
#     def game_players(player_name, player_bid):
#         players = {}
#         players["name"] = player_name
#         players["bid"] = player_bid
#         player_list.append(players)
#
#     more_bid = True
#     while more_bid:
#         name = input("What is your name?: ").title()
#         bid = int(input("What's your bid?: $"))
#         game_players(player_name=name, player_bid=bid)
#
#         other_bids = input("Are there any other bidders? Type y for 'yes' or n for 'no': ")
#         if other_bids == 'n':
#             print("-------------------------------------------")
#             more_bid = False
#
#     highest_bid = 0
#     highest_bidder = ""
#     for dictionary in player_list:
#         bid = dictionary["bid"]
#         if bid > highest_bid:
#             highest_bid = bid
#             highest_bidder = dictionary["name"]
#     print(f"The winner is {highest_bidder} with the highest bid of ${highest_bid}")
#
#
# secret_auction_game()
# ---------------------- Method 2 end -----------------------------
