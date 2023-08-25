from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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


def find_password():
    try:
        with open('data.json', 'r') as data:
            # read the data
            try:
                my_data = json.load(data)
            except json.decoder.JSONDecodeError:
                messagebox.showinfo(title="Website Not Found", message="No details for the website")
            else:
                if website_input.get() in my_data:
                    messagebox.showinfo(title=f"{website_input.get()}",
                                        message=f"Email: {my_data[website_input.get()]['email']} \nPassword: "
                                                f"{my_data[website_input.get()]['password']}")
                else:
                    messagebox.showinfo(title="Website Not Found",
                                        message="No details for the website")

    except FileNotFoundError:
        messagebox.showinfo(title="No File",
                            message="No Data File Found")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_input.get()
    password_name = password_input.get()
    email_address = email_input.get()
    new_data = {
        website_name: {
            "email": email_address,
            "password": password_name,
        }
    }

    if len(website_name) == 0 or len(password_name) == 0 or len(email_address) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty fields")

    else:
        try:
            with open('data.json', 'r') as data:
                # Reading old data
                my_data = json.load(data)
        except FileNotFoundError:
            with open('data.json', 'w') as data:
                # Creating new file if not present
                json.dump(new_data, data, indent=4)

        else:
            # Updating old data with new data
            my_data.update(new_data)
            with open('data.json', 'w') as data:
                # Saving updated data
                json.dump(my_data, data, indent=4)
        finally:
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
website_input = Entry(width=30)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=53)
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
gen_pass_button = Button(text="Generate Password", command=generate_password, width=18)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=18, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
