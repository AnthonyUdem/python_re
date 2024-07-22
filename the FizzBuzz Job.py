def fizzbuzz_game():
    """ Prints fizz if fully divisible by 3 and buzz if fully divisible by 5 then fizzbuzz if fully
    divisible by both 3 and 5. """

    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizzbuzz_game()
