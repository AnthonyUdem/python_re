def simple_calculator():
    """Simple calculator that calculates the +, -, *, /, modulo, and power operations"""
    from art import logo

    # Add
    def add(x, y):
        return x + y

    # Subtract
    def subtract(x, y):
        return x - y

    # Multiply
    def multiply(x, y):
        return x * y

    # Divide
    def divide(x, y):
        return x / y

    # Module
    def modulo(x, y):
        return x % y

    # Power
    def power(x, y):
        print("yes while power")
        return x ** y

    # Operators dictionary
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": modulo,
        "power": power,
    }

    def calculator():
        print(logo)
        print("Welcome to The Simple lonasctech Calculator.")
        num1 = float(input("Enter the first number: "))

        # Printing operator symbols
        symbols = ""
        for symbol in operations:
            symbols += symbol + "  "
        print(symbols)

        keep_calculating = True
        while keep_calculating:
            operation_symbol = input("Pick an operation: ")
            if operation_symbol not in operations:
                print("Please enter a valid operation!")
                keep_calculating = False
            else:
                num2 = float(input("Enter the next number: "))

                # getting the chosen operator
                get_function = operations[operation_symbol]
                answer = get_function(x=num1, y=num2)
                print(f"{num1} {operation_symbol} {num2} = {answer}")

                option = input(f"Type 'y' to continue with {answer} or type 'n' to start over or type 'x' to exit: ")
                if option == 'x':
                    keep_calculating = False
                elif option == 'y':
                    num1 = answer
                elif option == 'n':
                    keep_calculating = False
                    calculator()

    calculator()


simple_calculator()
