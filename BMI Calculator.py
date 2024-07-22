def bmi_calculator():
    """ Calculate and displays your BMI result """

    print("Welcome to Lonasctech BMI Calculator.")
    weight = float(input("What's your weight in kg: "))
    height = float(input("What's your height in meters: "))
    height_square = height ** 2
    bmi_result = round((weight/height_square), 2)
    if bmi_result < 18.5:
        print(f"Your BMI is {bmi_result}, you are underweight!")
    elif bmi_result < 25:
        print(f"Your BMI is {bmi_result}, you have a normal weight.")
    elif bmi_result < 30:
        print(f"Your BMI is {bmi_result}, you are overweight!")
    elif bmi_result < 35:
        print(f"Your BMI is {bmi_result}, you are obese!")
    else:
        print(f"Your BMI is {bmi_result}, you are clinically obese and need to a medical personnel!!")


bmi_calculator()
