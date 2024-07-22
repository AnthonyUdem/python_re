def treasure_island():
    """ Mission is to find the treasure. """

    print(''''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    ''')

    print("Welcome to the Treasure Island\nYour mission is to find the treasure.")
    direction = input("You're at a cross road. Where do you want to go? Type 'L' for left or 'R' for right: ").upper()
    if direction == 'L':
        option = input("You come to a lake. There is an island in the middle of the lake. \nType 'W' to wait for a boat"
                       " or 'S' to swim across.").upper()
        if option == 'W':
            color = input("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and"
                          " one blue. Which one do you choose? ").upper()
            if color == 'R':
                print("It's a room full of fire, you lose! Game Over.")
            elif color == 'B':
                print("You enter a room of beasts, Game Over!")
            elif color == 'Y':
                print("Congratulations! You Win🏆")
            else:
                print("Wrong option! please restart the game! and try again.")
        elif option == 'S':
            print("You got drown, Game Over!")
        else:
            print("Wrong option! please restart the game! and try again.")
    elif direction == 'R':
        print("You were hit by and unknown object, Game over!")
    else:
        print("Wrong option! please restart the game! and try again.")


treasure_island()
