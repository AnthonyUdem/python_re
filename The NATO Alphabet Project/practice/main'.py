# import random
# with open("file1.txt") as file1:
#     file1_data = file1.readlines()
#
# with open("file2.txt") as file2:
#     file2_data = file2.readlines()
#
# result = [int(num) for num in file2_data if num in file1_data]
# print(result)


# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}

# Conditional dictionary comprehension
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)
#
# passed_students = {student: score for (student, score)
#                    in student_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: round((temp_c*1.8 + 32), 2) for (day, temp_c) in weather_c.items()}
# print(weather_f)



# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# # looping through dictionaries
# for (keys, values) in student_dict.items():
#     print(f"{keys}: {values}")


# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for (keys, values) in student_data_frame.items():
#     print(keys)
#     print(values)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(index)
#     print(row.student)
#     print(row.score)
#     if row.student == "Angela":
#         print(row.score)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n*n for n in numbers]
# # print(squared_numbers)
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# # List comprehension
# # new_list = [new_item for item in list]
# list_num = [1, 3, 4]
# new_list = [n+1 for n in list_num]
# # print(new_list)
#
# # String as List
# names = "Anthony"
# letters_list = [letter for letter in names]
# # print(letters_list)
#
# # Range as list
# num_range_list = [n*2 for n in range(1, 5)]
# # print(num_range_list)
#
# # Conditional list comprehension
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)
