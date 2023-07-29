import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length_of_name = len(names)
random_pick = random.randint(0,length_of_name - 1)
print(f"{names[random_pick]} is going to buy the meal today!")
