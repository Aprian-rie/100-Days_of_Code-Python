from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


def button_clicked():
    my_label.config(text=input.get())


# Label

my_label = Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)


# Entry - Basically the Input
input = Entry(width=10)
print(input.get)
input.grid(column=3, row=2)








my_label.mainloop()
