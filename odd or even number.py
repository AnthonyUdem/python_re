def odd_or_even_number():
    """" Tell if a given number is odd or even """

    print("Welcome to Lonasctech odd or even number tester. This program would tell if a number is odd or even.")
    number = int(input("Put down the number you want to test: "))
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")


odd_or_even_number()
