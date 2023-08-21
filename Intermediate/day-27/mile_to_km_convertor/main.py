from tkinter import *


def miles_to_km_converter():
    miles = float(num_input.get())
    km = str(round(miles * 1.60934))
    answer_label.config(text=km)


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

num_input = Entry(width=7)
num_input.grid(row=0, column=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

answer_label = Label(text="0")
answer_label.grid(row=1, column=1)

SI_unit_label = Label(text="Km")
SI_unit_label.grid(row=1, column=2)

button = Button(text="Calculate", command=miles_to_km_converter)
button.grid(row=2, column=1)

window.mainloop()
