def food_menu():
    """ Allows users to enter the position where they want to place their secret food item and displays the food menu"""

    print("Welcome to the Food Menu")
    print("This program allows you to replace a food item on the menu to a secret item.\n")

    fruits = ["🥭", "🍉", "🍌", "🍍"]
    vegetables = ["🥕", "🍅", "🥒", "🥑"]
    sweets_desserts = ["🍦", "🎂", "🥪", "🍕"]

    food_items = [fruits, vegetables, sweets_desserts]
    print(f"{fruits} Fruits \n{vegetables} vegetables\n{sweets_desserts}  Sweets and desserts\n")

    position = input("Enter the roll: and column: of the item you wish to replace: ")
    column = int(position[0]) - 1
    roll = int(position[1]) - 1
    choice = food_items[column][roll]
    food_items[column][roll] = "🎁"

    print(f"{fruits} Fruits \n{vegetables} vegetables\n{sweets_desserts}  Sweets and desserts\n")
    print(f"{choice} was replaced with -> {food_items[column][roll]} - (There you have your secret item)")


food_menu()
