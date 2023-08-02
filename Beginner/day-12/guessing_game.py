#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
print("Welcome to the Number guessing game")
print("I'm thinking of a number between 1 to 100")
difficulty = input("Choose a difficulty between 'easy' and 'hard': ")
if difficulty == "easy":
  no_chances = 10
elif difficulty == "hard":
  no_chances = 5
guess_list = []
for guess in range (1,101):
  guess_list.append(guess)
computer_choice = random.choice(guess_list)
user_wins = False
def cmp(one,two):
  if one > two:
    return (1)
  elif one < two:
    return (-1)
  elif one == two:
    return (0)
while no_chances > 0 and user_wins == False:
  print(f"You have {no_chances} attempts to guess the number")
  user_choice = int(input("Make a guess: "))
  comparison = cmp(user_choice, computer_choice)
  if comparison == -1:
    print("Too low")
    print("Guess Again")
  elif comparison == 1:
    print("Too high")
    print("Guess Again")
  elif comparison == 0:
    print("You win")
    user_wins = True
  no_chances -= 1
