# The Python File System

# file = open("my_file.txt")  # Opens the file
# contents = file.read()
# print(contents)
# file.close()   # Closes the file

with open("my_file.txt") as file:  # Opens and close the file automatically
    contents = file.read()
    print(contents)

# with open("my_file.txt", mode="w") as file:  # Opens and close the file automatically
#     file.write("Hello Philor")      # mode="w" -> Writes to the file by deleting the exiting text in the file

# with open("my_file.txt", mode="a") as file:  # Opens and close the file automatically
#     file.write(" Philorcardium")    # mode="a" -> Writes to the file by appending to the exiting text in the file
#

# #This format can create a new file if they are not already created in the working folder
# with open("new_file.txt", mode="w") as file:  # Opens and close the file automatically
#     file.write("Hello Philor\nGlad to have you here.")  # mode="w" -> Writes to the file by deleting the exiting
#                                                         # text in the file
#
