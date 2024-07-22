def average_height():
    """ requires a list of student's height and display the average height """

    # ======== Methode 3 - python =============================
    student_heights = input("Input a list of student heights: ").split()
    for height in range(0, len(student_heights)):  # range function does not include the last number
        student_heights[height] = int(student_heights[height])
    sum_of_heights = sum(student_heights)
    numbers_of_heights = len(student_heights)
    average = round(sum_of_heights / numbers_of_heights)  # round the floating number into whole
    print(f"Number of input heights: {numbers_of_heights}\nThe sum total height is: {sum_of_heights}"
          f"\nAnd the average is: {average} -> to the nearest whole number")
    # ============== Method 1 end =============================

    # ============== Method 2 ==================================
    # add_height = 0
    # student_heights = input("Input a list of student heights: ").split()
    # for height in student_heights:
    #     add_height += int(height)
    # count = 0
    # for student in student_heights:
    #     count += 1
    # average = "{:.0f}".format(add_height/count)    # round the floating number to a whole number.
    # print(f"The sum total height is: {add_height}\nThere are number of {count} height\nAnd the average is: {average} "
    #       f"-> to the nearest whole number")

    # ============== Method 2 end ===============================

    # ============== Method 3 general ===========================
    # add_height = 0
    # count = 0
    # student_heights = input("Input a list of student heights: ").split()
    # for height in range(0, len(student_heights)):  # range function does not include the last number
    #     student_heights[height] = int(student_heights[height])
    #     add_height += student_heights[height]
    # for student in student_heights:
    #     count += 1
    # average = "{:.0f}".format(add_height / count)  # round the floating number to a whole number.
    # print(f"The sum total height is: {add_height}\nThere are number of {count} height\nAnd "
    #       f"the average is: {average} -> to the nearest whole number")
    # ============== Method 3 end ===============================


average_height()

#
# 4 5 9 2 1 1
# 180 124 165 173 189 169 146
