def check_prime():
    """ Has prime_number_checker as a function """
    def prime_number_checker(number):
        """ request for a number and print if it's a prime number or not """

        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False

        if number == 1 or number == 0:
            print(f"{number} is not a prime number")
        elif is_prime:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")

    print("Welcome to The Lonasctech Prime Number Checker.\n"
          "This program would tell if the number you enter is a prime number or not.\n")
    n = int(input("Enter the number: "))
    prime_number_checker(number=n)


check_prime()
