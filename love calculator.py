def love_calculator():
    """ Requires two names from the user and displays their love score """""

    print("Welcome to The Lonasctech Love Calculator")
    print("This calculator requires you to input two names and it would displays their love score")
    first_name = input("What is your name? ").lower()
    second_name = input("What is their name? ").lower()
    t_f = first_name.count("t")
    r_f = first_name.count("r")
    u_f = first_name.count("u")
    e_f = first_name.count("e")

    t_s = second_name.count("t")
    r_s = second_name.count("r")
    u_s = second_name.count("u")
    e_s = second_name.count("e")

    sum_true = str(t_f + r_f + u_f + e_f + t_s + r_s + u_s + e_s)

    l_f = first_name.count("l")
    o_f = first_name.count("o")
    v_f = first_name.count("v")
    e_f = first_name.count("e")

    l_s = second_name.count("l")
    o_s = second_name.count("o")
    v_s = second_name.count("V")
    e_s = second_name.count("e")

    sum_love = str(l_f + o_f + v_f + e_f + l_s + o_s + v_s + e_s)

    score = int(sum_true + sum_love)
    if 10 > score > 90:
        print(f"Your score is: {score}%, you go together like coke and mentos❤️.")
    elif 40 <= score <= 50:
        print(f"Your score is: {score}%, you are alright together❤️.")
    else:
        print(f"Your score is {score}%, you go together like beans and rice❤️")


love_calculator()
# Arianna Rebolini
# Channing Tatum
# Kanye west
# Kim kardashian
