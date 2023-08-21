from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New text")


# Button

def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry - Basically the Input

input = Entry(width=10)
input.pack()















my_label.mainloop()
