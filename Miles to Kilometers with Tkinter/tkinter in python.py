from tkinter import *
# Window a new window and configurations
window = Tk()
window.title("Lonasctech GUI Program")
window.minsize(width=500, height=500)

# Labels
label = Label(text="I'm a label", font=("Arial", 20, "normal"))
label["text"] = "Changed text"
label.config(text="New config text")
label.pack()

# Buttons
def button_clicked():
    label.config(text=entry.get(), font=("Arial", 20, "bold"))
    
# Calls action() when pressed
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string=" some text to begin with.")
# Get text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, " example of multi - line text entry.")
# Get current value in textbox at line 1, character 0
print(text.get("1.3", END))
text.pack()

# Spinbox
def spinbox_used():
    # get the current value in spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scare
# Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    # prints 1 if on button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()




window.mainloop()





# Unlimited Positional arguments in function call/declaration
# def add(*numbers):
#     print(numbers[2])
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

# Optional 'key word arguments' (kwargs)
# def calculate(n, **kwargs):
#     # print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     # print(n)
#
# calculate(2, add=3, multiply=5)

# class Car:
#     def __int__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.colour = kw.get("colour")
#         self.seats = kw.get("seats")

# my_car = Car(make="farari", model="HD-9")
# print(my_car)
