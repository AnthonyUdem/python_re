def days_in_a_month():
    """ requires the year and month, then print the number of days in the month """

    def is_leap(the_year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def days_in_month(in_year, in_month):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if in_month > 12 or in_month < 1:
            return "Please enter a valid month between 1 and 12"
        if is_leap(in_year) and in_month == 2:
            return f"There are: 29 days"
        else:
            return f"There are: {month_days[in_month - 1]} days"

    print("Welcome to The Lonasctech Days in a Month Calculator.")
    year = int(input("Enter a year: "))
    month = int(input("Enter a month, 'in number': "))

    days = days_in_month(in_year=year, in_month=month)
    print(days)


days_in_a_month()
