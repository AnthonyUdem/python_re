def tip_calculator():
    """ shares a bill tip among x people and displays the result """

    print("Welcome to Lonasctech bill-tip calculator")
    print("This program would shares a bill tip among x people and displays the result")
    bill_amount = float(input("What was the total bill? $"))
    tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
    split_number = int(input("How many people to slit the bill? "))
    split_amount = bill_amount + (bill_amount * tip/100)
    amount_per_each = "{:.2f}".format(split_amount/split_number)
    print(f"Each person should pay: ${amount_per_each}")


tip_calculator()
