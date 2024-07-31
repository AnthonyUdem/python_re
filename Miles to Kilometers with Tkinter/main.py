from tkinter import *

window = Tk()
window.title("Lonasctech Mile to Km Converter")
window.config(padx=20, pady=20)

mile_entry = Entry(width=6, font=("Arial", 14, "bold"))
mile_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal = Label(text="is equal to", font=("Arial", 14))
is_equal.grid(column=0, row=1)
is_equal.config(padx=10, pady=10)

def km_result():
    result = round(float(mile_entry.get()) * 1.609344, 2)
    kilo_m_entry.insert(END, string=f"{result}")

kilo_m_entry = Entry(width=10, font=("Arial", 14, "bold"))
kilo_m_entry.grid(column=1, row=1)

kilo_m = Label(text="Km", font=("Arial", 14))
kilo_m.grid(column=2, row=1)
kilo_m.config(padx=10, pady=10)

cal_but = Button(text="Calculate", font=("Arial", 10, "bold"), command=km_result)
cal_but.grid(column=1, row=2)
cal_but.config(padx=5, pady=5)


window.mainloop()
