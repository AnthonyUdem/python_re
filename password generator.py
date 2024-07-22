import random


def password_generator():
    """ Generates a random number of password from user's number input """

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to The Lonasctech Password Generator!")
    print("This program will generate you a random password bass on the number you want.")
    num_letters = int(input("How many letters would you like in your password? "))
    num_symbols = int(input(f"How many symbols would you like? "))
    num_numbers = int(input(f"How many numbers would you like? "))

    # ================== Method 1 ==========================
    password = []
    for letter in range(0, num_letters):
        password.append(random.choice(letters))

    for symbol in range(0, num_symbols):
        password += random.choice(symbols)

    for number in range(0, num_numbers):
        password += random.choice(numbers)

    random.shuffle(password)
    print(f"Here is your password: {"".join(password)} 🔒")  # shuffled password

    # ------------------------ OR ------------
    # password_or = ""
    # for char in password:
    #     password_or += char
    # print(f"Here is your password: {password_or 🔒}")     # shuffled password
    # ================== Method 1 end ===========================

    # ================== Method 2 ===============================
    # password = ""
    # for letter in range(0, num_letters):
    #     password += random.choice(letters)
    #
    # for symbol in range(0, num_symbols):
    #     password += random.choice(symbols)
    #
    # for number in range(0, num_numbers):
    #     password += random.choice(numbers)
    #
    # print(f"Here is your password: {password}")       # password is not shuffled
    # ================== Method 2 end ===========================

    # =================== Method 3 ===============================
    # random_letters = []
    # for n in range(0, num_letters):
    #     random_letters.append(random.choice(letters))
    #
    # random_symbols = []
    # for n in range(0, num_symbols):
    #     random_symbols.append(random.choice(symbols))
    #
    # random_numbers = []
    # for n in range(0, num_numbers):
    #     random_numbers.append(random.choice(numbers))
    #
    # password = "".join(random_letters) + "".join(random_symbols) + "".join(random_numbers)
    # print(f"Here is your password: {password}")     # password is not shuffled
    # ================== Methode 3 end ===========================


password_generator()

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
