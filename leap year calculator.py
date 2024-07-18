def leap_year():
    """"Calculate and displays if a year is leap year or not"""

    print("Welcome to Lonasctech leap year calculator.")
    year = int(input("What year do you want to check? "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


leap_year()
