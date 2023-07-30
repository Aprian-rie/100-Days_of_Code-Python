#Step 1 

import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_guess = (input("Guess a letter: ")).lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#chosen_word = word_list[random.randint(0,2)]
for letter in chosen_word:
  if letter == user_guess:
    print("It is the one !")
  else:
      print("Not the one")
