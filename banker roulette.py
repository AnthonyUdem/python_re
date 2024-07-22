import random


def bank_roulette():
    """Request names of people involve and displays a random bill payer."""
    # put the names into a list separated by comma
    user_names = input("Put down everyone name separated by a comma: ").split(", ")
    print(user_names)
    # number_of_names = len(user_names)
    # random_name = random.randint(0, (number_of_names-1))
    # bill_payer = user_names[random_name]

    bill_payer = random.choice(user_names)
    print(f"{bill_payer} is buying the meal today.")


bank_roulette()
# Mary, Edward, Chinaza, Victory, Jessica, Emeka, Peter, Daniel, Emmanuel,
# Anthony, Ben, James, Isaiah, Joshua
