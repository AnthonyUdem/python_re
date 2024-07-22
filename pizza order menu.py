def pizza_deliveries():
    """" Ask the user for the pizza size, pepperoni and extra cheese """

    print(f"Welcome to The Lonasctech Pizza Deliveries")
    print(f"Small pizza is $15\nMedium pizza is $20\nLarge pizza is $25\n---------------------------------")
    size = input("What size of pizza do you want?\nType 'S' for small, 'M' for medium, and 'L' for large: ").upper()
    add_pepperoni = input("Do you want pepperoni? 'Y' or 'N' : ").upper()
    extra_cheese = input("Do you want extra cheese? 'Y' or 'N' : ").upper()

    if size == 'S':
        prize = 15
        if add_pepperoni == 'Y':
            prize += 2
            if extra_cheese == 'Y':
                prize += 1
        print(f"Here is your pizza 🍕\nYour final bill is: ${prize}\n-----------------------------"
              f"-----\nThank you for patronizing us")

    elif size == 'M':
        prize = 20
        if add_pepperoni == 'Y':
            prize += 3
            if extra_cheese == 'Y':
                prize += 1
        print(f"Here is your pizza 🍕\nYour final bill is: ${prize}\n----------------------------"
              f"------\nThank you for patronizing us")
    elif size == 'L':
        prize = 25
        if add_pepperoni == 'Y':
            prize += 3
            if extra_cheese == 'Y':
                prize += 1
        print(f"Here is your pizza 🍕\nYour final bill is: ${prize}\n-------------------------------"
              f"---\nThank you for patronizing us")
    else:
        print("Please re-start the program and pick a valid option")


pizza_deliveries()
