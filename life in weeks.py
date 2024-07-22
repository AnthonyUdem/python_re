def time_left():
    """ Calculates and displays the numbers of days, weeks, and months left from someone's ege up to 90 """
    days = 365
    weeks = 52
    months = 12
    print("Welcome to Lonasctech.\nThis program will calculate and displays the remaining days, weeks, and months left"
          " in your age if you were to life up to 90 years.")
    age = int(input("What's your age this year? "))
    age_left = 90 - age
    message = (f"There are {age_left*days} days, {age_left*weeks} weeks, and {age_left*months} months left to live "
               f"withing age {age} and 90 ")
    print(message)


time_left()
