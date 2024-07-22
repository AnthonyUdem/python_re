def paint_area():
    """Has cal_paint_number as a function"""

    def cal_paint_number(height, width, coverage):
        """ Allow users to input the height, and width of wall they want to paint, then print the
        number of cans needed """

        wall_area = height * width
        num_of_paints = round(wall_area / coverage)  # round the value to a whole number

        if num_of_paints == 1:
            print(f"\nYou just need a can of paint 🧳")
        elif num_of_paints > 1:
            print(f"\nYou'll need {num_of_paints} cans of paint 🧳")
        else:
            print(f"\nSeems you don't need a paint at all")

    print("Welcome to The Lonasctech 'Paint Can' Calculator.\n")
    print("This program allows you to input the height and width (in meters) of the wall \nyou want to get paint for, "
          "and then, displays the number of paint\nneeded in the nearest whole number.\nWhere one 'can' of "
          "paint covers 5 "
          "square meters\n")

    height_val = float(input("Enter the height of the wall: "))
    width_val = float(input("Enter the width of the wall: "))
    cal_paint_number(height=height_val, width=width_val, coverage=5)


paint_area()
