from tkinter import *
from time import time
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ------- READING DATA FROM CSV FILE -------------------
words_data = pandas.read_csv('data/french_words.csv')
french_words = words_data['French']
french_words_list = french_words.to_list()


# print(french_words_list)

# --------- Generating random french word ---------------
def generate_random_words():
    canvas.delete("french_tag")
    canvas.delete("english_tag")
    random_french_word = random.choice(french_words_list)
    english_word_corr = words_data['English'][words_data.French == random_french_word]
    canvas.create_text(380, 250, text=random_french_word, fill="black", font='Helvetica 35 bold', tags="french_tag")
    window.after(3000, display_english(english_word_corr))


def display_english(english_word):
    canvas.create_text(380, 250, text=english_word, fill="black", font='Helvetica 35 bold', tags="english_tag")


# def timer():
#     window.after(3000, )
# ----------------- UI SETUP ----------------------------
window = Tk()
window.title('FlashCardApp')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=530)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(380, 150, text="French", fill="black", font='Helvetica 25 italic')
# canvas.create_text(380, 150, text="French", fill="black", font='Helvetica 25 italic')
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_button = Button(command=generate_random_words)
cross_image = PhotoImage(file="images/wrong.png")
cross_button.config(image=cross_image, highlightthickness=0)
cross_button.grid(row=1, column=0)

tick_button = Button(command=generate_random_words)
tick_image = PhotoImage(file="images/right.png")
tick_button.config(image=tick_image, highlightthickness=0)
tick_button.grid(row=1, column=1)

window.mainloop()
