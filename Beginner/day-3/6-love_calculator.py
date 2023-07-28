# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()
name_combined = name1_lower + name2_lower
t_count = name_combined.count("t")
r_count = name_combined.count("r")
u_count = name_combined.count("u")
e_count = name_combined.count("e")
total1 = t_count + r_count + u_count + e_count

l_count = name_combined.count("l")
o_count = name_combined.count("o")
v_count = name_combined.count("v")
total2 = l_count + o_count + v_count + e_count

grand_total = str(total1) + str(total2)
if grand_total < "10" or grand_total > "90":
  print(f"Your score is {grand_total}, you go together like coke and mentos.")
elif grand_total > "40" and grand_total < "50":
  print(f"Your score is {grand_total}, you are alright together.")
else:
  print(f"Your score is {grand_total}.")
