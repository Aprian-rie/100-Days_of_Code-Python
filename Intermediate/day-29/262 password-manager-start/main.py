from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list_letters = [random.choice(letters) for letter in range(0, nr_letters)]
    password_list_symbols = [random.choice(symbols) for symbol in range(0, nr_symbols)]
    password_list_numbers = [random.choice(numbers) for number in range(0, nr_numbers)]

    password_list = password_list_numbers + password_list_letters + password_list_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_input.get()
    password_name = password_input.get()
    email_address = email_input.get()

    if len(website_name) == 0 or len(password_name) == 0 or len(email_address) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty fields")

    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"These are the details entered: \nEmail: {email_address}"
                                               f" \nPassword:{password_name} \nIs it okay to save?")
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f"{website_name} | {email_address} | {password_name}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Rie's Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo_rie (2).png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Inputs
website_input = Entry(width=48)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=48)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'rie@gmail.com')

password_input = Entry(width=30)
password_input.grid(row=3, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Buttons
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=41, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
