def roller_coaster():
    """ A simple roller-coaster with pictures taken on the way. """

    print("Welcome to the roller-coaster!")
    name = input("What is your name: ").title()
    hight = int(input("What is your hight in cm? "))
    # bill = 0
    if hight >= 120:
        age = int(input("How old are you? "))
        if age < 12:
            bill = 5
            print(f"Children tickets are ${bill}.")
        elif age <= 18:
            bill = 7
            print(f"Youth tickets are ${bill}.")
        elif 45 <= age <= 55:
            bill = 0
            print(f"Everything is going to be okay, have a free ride on us. Tickets withing ages [45 - 55] is free - $0")
        else:
            bill = 12
            print(f"Adult tickets are ${bill}.")
        photo = input(f"{name} do you want a photo taken while on the roller_coaster?\nType 'Y' for yes and 'N' for no: ").upper()
        if photo == 'N':
            print(f"Your final bill is ${bill}.\nThank you for patronizing lonasctech")
        elif photo == 'Y':
            bill += 3
            print(f"Your final bill is ${bill}\nThank you for patronizing lonasctech")
        else:
            print("Please restart the game and enter a valid option!")
    else:
        print("Sorry, you have to grow taller before you can ride! powering off.")


roller_coaster()
