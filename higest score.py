def highest_score():
    """ request for a list of numbers and display the highest score """

    # ==================== Method 1 python  =================================
    print("This program will display the highest number in a list.")
    student_scores = input("Put down the list of numbers: ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    highest = max(student_scores)
    print(student_scores)
    print(f"The highest score is: {highest}")
    # ==================== Method 1 end =================================

    # ==================== Method 2 general =============================
    # print("This program will display the highest number in a list.")
    # student_scores = input("Put down the list of numbers: ").split()
    # highest = 0
    # for n in range(0, len(student_scores)):
    #     student_scores[n] = int(student_scores[n])
    # for score in student_scores:
    #     if score > highest:
    #         highest = score
    # print(student_scores)
    # print(f"The highest score is: {highest}")
    # ==================== Method 2 end =================================

    # ==================== Method 3 general ===============================
    # print("This program will display the highest number in a list.")
    # student_scores = input("Put down the list of numbers: ").split()
    # highest = 0
    # for score in range(0, len(student_scores)):
    #     student_scores[score] = int(student_scores[score])
    #     if student_scores[score] > highest:
    #         highest = student_scores[score]
    # print(student_scores)
    # print(f"The highest score is: {highest}")
    # ==================== Method 3 end =================================


highest_score()
# 80 124 65 123 18 -2 0 1 120
