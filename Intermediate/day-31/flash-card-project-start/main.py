from tkinter import *
from time import time
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ------- READING DATA FROM CSV FILE -------------------
try:
    words_data = pandas.read_csv('data/Words to learn.csv')
except FileNotFoundError:
    og_words_data = pandas.read_csv("data/french_words.csv")
    to_learn = og_words_data.to_dict(orient="records")
else:
    to_learn = words_data.to_dict(orient="records")


# print(french_words_list)

# --------- Generating random french word ---------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/Words to learn.csv", index=False)
    next_card()


# ----------------- UI SETUP ----------------------------
window = Tk()
window.title('FlashCardApp')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=530)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(380, 150, text="Title", fill="black", font='Ariel 25 italic')
card_word = canvas.create_text(380, 250, text="Word", fill="black", font='Ariel 35 bold')
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_button = Button(command=next_card)
cross_image = PhotoImage(file="images/wrong.png")
cross_button.config(image=cross_image, highlightthickness=0)
cross_button.grid(row=1, column=0)

tick_button = Button(command=is_known)
tick_image = PhotoImage(file="images/right.png")
tick_button.config(image=tick_image, highlightthickness=0)
tick_button.grid(row=1, column=1)

next_card()
window.mainloop()
