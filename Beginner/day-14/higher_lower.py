import art 
import random
import game_data
from replit import clear

figure_1 = random.choice(game_data.data)
figure_2 = random.choice(game_data.data)
while figure_1 == figure_2:
  figure_2 = random.choice(data)
def ask_user():
  print(f"Compare A: {figure_1['name']}, {figure_1['description']}, from {figure_1['country']}")
  print(art.vs)
  print(f"Compare B: {figure_2['name']}, {figure_2['description']}, from {figure_2['country']}")
  
  
game_over = False
score_count = 0
while not game_over:
  print(art.logo)
  if score_count > 0:
    print(f"You're right current score is {score_count}")
  ask_user()
  user_choice_string = input("Who has more followers A or B: ")
  if user_choice_string == "A":
    user_choice_input = figure_1["follower_count"]
    if user_choice_input > figure_2["follower_count"]:
      score_count += 1
    else:
      game_over = True
  elif user_choice_string == "B":
    user_choice_input = figure_2["follower_count"]
    if user_choice_input > figure_1["follower_count"]:
      score_count += 1
    else:
      game_over = True
  clear()
  figure_1 = figure_2
  figure_2 = random.choice(game_data.data)
print(f"Sorry, that's wrong you're final score is {score_count}")
