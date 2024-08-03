import pandas
# TODO 1. Create a dictionary in this format:
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_frame = pandas.DataFrame(nato_data)
nato_data_dic = {row.letter: row.code for (index, row) in nato_frame.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_list = [letter.upper() for letter in input("Enter a word: ")]
user_nato_phonetic_list = [nato_data_dic[char] for char in user_list if char in nato_data_dic]
# ------------------------ Method 2 ------------------------
# for char in user_list:
#     for key in nato_dic:
#         if char == key:
#             user_nato_list.append(nato_dic[char])
print(user_nato_phonetic_list)
