# -------------------------------------- Method 2 --------------------------------------------#
# from menu import resources
# from menu import MENU
# from art import logo
#
# print(logo)
# print("Hello! Welcome to The Lonasctech Coffee Machine.")
#
#
# def off_machine():
#     """Turn off the coffee machine and stop the program."""
#     global machine_is_on
#     machine_is_on = False
#     print("Powering off...✔️")
#
#
# def display_menu():
#     """Display the menu to the user"""
#     print("\n'1'  Turn off The Coffee Machine!")
#     print("'2'  Available drinks")
#     print("'3'  Display the resources")
#     option = int(input("\nEnter a number from the list📝 above: "))
#     return option
#
#
# def execute_menu(menu):
#     """Executes the chosen menu from the user input and set the drink name"""
#     global drink_name
#
#     if menu == 1:
#         off_machine()
#     elif menu == 2:
#         name = input("What would you like?\nType \n'e' for espresso 🍷 "
#                      "\n'l' for latte 🥃  or \n'c' for cappuccino 🍺: ").lower()
#         if name == "e":
#             drink_name = "espresso"
#         elif name == "l":
#             drink_name = "latte"
#         elif name == "c":
#             drink_name = "cappuccino"
#         else:
#             print("❌ You input a wrong letter, please enter either 'e', or 'l', or 'c'.")
#             run_machine()
#     elif menu == 3:
#         if drink_name != "espresso":
#             print(f"Water:  💧  {resource_water}ml\nMilk:   🥛  {resource_milk}ml\n"
#                   f"Coffee: ☕  {resource_coffee}g\nMoney:  💰  ${resource_money}")
#             run_machine()
#         else:
#             print(f"Water:  💧  {resource_water}ml\nMilk:   🥛  {resource_milk + drink_milk}ml\n"
#                   f"Coffee: ☕  {resource_coffee}g\nMoney:  💰  ${resource_money}")
#             run_machine()
#     else:
#         print("❌ You input a wrong number, please enter either '1', or '2' or '3'.")
#         run_machine()
#
#
# def get_drink_name():
#     """Gets hold of the chosen drink name from the MENU dictionary."""
#     global drink_name
#     for key in MENU:
#         if key == drink_name:
#             drink_name = key
#
#
# def get_drink_resource():
#     """Get and set the drink resource from the MENU dictionary."""
#     global drink_cost, drink_water, drink_milk, drink_coffee, drink_name
#
#     drink_cost = MENU[drink_name]["cost"]
#     get_ingredient = MENU[drink_name]["ingredients"]
#     if drink_name == "espresso":
#         drink_water = get_ingredient["water"]
#         drink_coffee = get_ingredient["coffee"]
#     else:
#         drink_water = get_ingredient["water"]
#         drink_milk = get_ingredient["milk"]
#         drink_coffee = get_ingredient["coffee"]
#
#
# def check_resource_sufficient():
#     """Checks if the transaction is successful, print a statement if not successful, and re-run the coffee machine"""
#     global drink_cost, drink_water, drink_milk, drink_coffee, drink_name, \
#         resource_water, resource_milk, resource_coffee, resource_money
#
#     if drink_name != "espresso":
#         if drink_water > resource_water:
#             print(f"❌ Sorry, there is not enough water!")
#             run_machine()
#         elif drink_milk > resource_milk:
#             print(f"❌ Sorry, there is not enough milk!")
#             run_machine()
#         elif drink_coffee > resource_coffee:
#             print(f"❌ Sorry, there is not enough coffee!")
#             run_machine()
#     elif drink_water > resource_water:
#         print(f"❌ Sorry, there is not enough water!")
#         run_machine()
#         if drink_coffee > resource_coffee:
#             print(f"❌ Sorry, there is not enough coffee!")
#             run_machine()
#
#
# def process_coin():
#     """Get all the user inserted coins and returns their total"""
#     print("\nPleas insect coins.")
#     total = float(input("How many quarters?: ")) * 0.2
#     total += float(input("How many dimes?: ")) * 0.10
#     total += float(input("How many nickels?: ")) * 0.05
#     total += float(input("How many pennies?: ")) * 0.01
#     return total
#
#
# def check_transaction(enough_coin, cost_of_drink):
#     """Get the processed coin value and drink cost to check if transaction is possible, then,
#      add money to resources and refund change, or refund the money if not enough coins."""
#     global drink_name
#
#     if enough_coin >= cost_of_drink:
#         change = round((enough_coin - cost_of_drink), 2)
#         resources["Money"] = f"${drink_cost}"
#         print(f"\nHere is ${change} in change.")
#         print(f"Cost of {drink_name} is: ${cost_of_drink}")
#         return True
#     else:
#         print(f"\n❌ Sorry that's not enough money. Money refunded! ${round(enough_coin, 2)},  "
#               f"cost of {drink_name} is ${drink_cost}")
#         return False
#
#
# def make_coffee(successful):
#     """Get the transaction status as an argument and make the coffee if successful.
#     Then, deducts the required ingredients from the resources"""
#
#     global drink_name, resource_water, resource_milk, resource_coffee, resource_money
#     if successful:
#         resource_water -= drink_water
#         resource_milk -= drink_milk
#         resource_coffee -= drink_coffee
#         resource_money += drink_cost
#         print(f"Here is your {drink_name} ☕.  Enjoy!😃")
#
#
# drink_water = 0
# drink_milk = 0
# drink_coffee = 0
# drink_cost = 0
#
# drink_name = ""
# resource_water = resources["water"]
# resource_milk = resources["milk"]
# resource_coffee = resources["coffee"]
# resource_money = 0
#
# machine_is_on = True
#
#
# def run_machine():
#     while machine_is_on:
#         menu = display_menu()  # ✔️
#         execute_menu(menu)  # ✔️
#         get_drink_name()  # ✔️
#
#         if machine_is_on:
#             get_drink_resource()  # ✔️
#             check_resource_sufficient()  # ✔️
#             enough_coins = process_coin()  # ✔️
#             trans_successful = check_transaction(enough_coins, drink_cost)  # ✔️
#             make_coffee(trans_successful)  # ✔️
#
#
# run_machine()

# -------------------------------------- Method 2 end ------------------------------------------#

# # -------------------------------------- Method 1 Angela Yu------------------------------------------#
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
#
# # -------------------------------------- Method 1 end ----------------------------------------#

# #-------------------------------------- Method 3 --------------------------------------------#

from menu import resources
from menu import MENU
from art import logo
print(logo)
print("Hello! Welcome to The Lonasctech Coffee Machine.")

def off_machine():
    """Turn off the coffee machine and stop the program."""
    global machine_is_on
    machine_is_on = False
    print("Powering off...✔️")
def display_menu():
    """Display the menu to the user"""
    print("\n'1'  Turn off The Coffee Machine!")
    print("'2'  Available drinks")
    print("'3'  Display the resources")
    option = int(input("\nEnter a number from the list📝 above: "))
    return option
def process_coin(quarter, dime, nickel, pennie):
    """Get all the user inserted coins and returns their sum"""
    user_coins = (0.2 * quarter) + (0.10 * dime) + (0.05 * nickel) + (0.01 * pennie)
    return user_coins
def check_transaction(enough_coin, cost_of_drink):
    """Get the processed coin value and drink cost to check if transaction is possible, then,
     add money to resources and refund change, or refund the money if not enough coins."""
    global drink_name
    if enough_coin >= cost_of_drink:
        change = round((enough_coin - cost_of_drink), 2)
        resources["Money"] = f"${drink_cost}"
        print(f"\nHere is ${change} in change.")
        print(f"Cost of {drink_name} is: ${cost_of_drink}")
        return True
    else:
        print(f"\n❌ Sorry that's not enough money. Money refunded! ${round(enough_coin, 2)},  "
              f"cost of {drink_name} is ${drink_cost}")
        return False


drink_water = 0
drink_milk = 0
drink_coffee = 0
drink_cost = 0

drink_name = ""
resource_water = resources["water"]
resource_milk = resources["milk"]
resource_coffee = resources["coffee"]
resource_money = 0

machine_is_on = True
def run_machine():
    while machine_is_on:
        global drink_cost, drink_water, drink_milk, drink_coffee, drink_name, \
            resource_water, resource_milk, resource_coffee, resource_money

        menu = display_menu()
        if menu == 1:
            off_machine()
        elif menu == 2:
            name = input("What would you like?\nType \n'e' for espresso 🍷 "
                         "\n'l' for latte 🥃  or \n'c' for cappuccino 🍺: ").lower()
            if name == "e":
                drink_name = "espresso"
            elif name == "l":
                drink_name = "latte"
            elif name == "c":
                drink_name = "cappuccino"
            else:
                print("❌ You input a wrong letter, please enter either 'e', or 'l', or 'c'.")
                run_machine()
        elif menu == 3:
            if drink_name != "espresso":
                print(f"Water:  💧  {resource_water}ml\nMilk:   🥛  {resource_milk}ml\n"
                      f"Coffee: ☕  {resource_coffee}g\nMoney:  💰  ${resource_money}")
                run_machine()
            else:
                print(f"Water:  💧  {resource_water}ml\nMilk:   🥛  {resource_milk + drink_milk}ml\n"
                      f"Coffee: ☕  {resource_coffee}g\nMoney:  💰  ${resource_money}")
                run_machine()

        else:
            print("❌ You input a wrong number, please enter either '1', or '2' or '3'.")
            run_machine()

        for key in MENU:
            if key == drink_name:
                drink_name = key

        if machine_is_on:
            drink_cost = MENU[drink_name]["cost"]
            get_ingredient = MENU[drink_name]["ingredients"]
            if drink_name == "espresso":
                drink_water = get_ingredient["water"]
                drink_coffee = get_ingredient["coffee"]
            else:
                drink_water = get_ingredient["water"]
                drink_milk = get_ingredient["milk"]
                drink_coffee = get_ingredient["coffee"]

            if drink_name != "espresso":
                if drink_water > resource_water:
                    print(f"❌ Sorry, there is not enough water!")
                    run_machine()
                elif drink_milk > resource_milk:
                    print(f"❌ Sorry, there is not enough milk!")
                    run_machine()
                elif drink_coffee > resource_coffee:
                    print(f"❌ Sorry, there is not enough coffee!")
                    run_machine()

            elif drink_water > resource_water:
                print(f"❌ Sorry, there is not enough water!")
                run_machine()
                if drink_coffee > resource_coffee:
                    print(f"❌ Sorry, there is not enough coffee!")
                    run_machine()


            print("\nPleas insect coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            enough_coins = process_coin(quarters, dimes, nickels, pennies)
            trans_successful = check_transaction(enough_coins, drink_cost)
            # make_coffee
            if trans_successful:
                resource_water -= drink_water
                resource_milk -= drink_milk
                resource_coffee -= drink_coffee
                resource_money += drink_cost
                print(f"Here is your {drink_name} ☕  Enjoy!😁")


run_machine()
# #-------------------------------------- Method 3 end --------------------------------------------#
