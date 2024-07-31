from tkinter import *
# Buttons
def button_clicked():
    label.config(text=entry.get(), font=("Arial", 20, "bold"))

window = Tk()
window.title("Lonasctech GUI Program")
window.minsize(width=500, height=400)
window.config(padx=50, pady=50)

label = Label(text="I'm a label", font=("Arial", 12, "bold"))
label["text"] = "Changed text"
label.config(text="New config text")
label.place(x=0, y=0)
label.grid(column=0, row=0)
# label.pack()

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=5, pady=5)
# button.pack()
# button.place(x=10,y=20)

new_button = Button(text="New button", command=button_clicked)
new_button.grid(column=2, row=0)
new_button.config(padx=5, pady=5)

entry = Entry(width=50)
entry.insert(END, string=" some text to begin with.")
print(entry.get())
entry.grid(column=3, row=3)
# entry.pack()

window.mainloop()
