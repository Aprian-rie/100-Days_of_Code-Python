import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
selectables = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
AI_choice = random.randint(0,2)
print(selectables[user_choice])
print("Computer chose: ")
print(selectables[AI_choice])
if user_choice == AI_choice:
  print("It's a draw ! Can't beat the AI eeh try again")
elif (user_choice == 0 and AI_choice == 1) or (user_choice == 1 
 and AI_choice == 2) or (user_choice == 2 and AI_choice == 0) :
  print("You Lose!")
elif (user_choice == 0 and AI_choice == 2) or (user_choice == 1 
 and AI_choice == 0) or (user_choice == 2 and AI_choice == 1) :
  print("You Win!")
