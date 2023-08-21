from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Rie's Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo_rie (2).png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_input = Entry(width=48)
website_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=48)
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=30)
password_input.grid(row=3, column=1)

gen_pass_button = Button(text="Generate Password")
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=41)
add_button.grid(row=4, column=1, columnspan=2)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)












window.mainloop()