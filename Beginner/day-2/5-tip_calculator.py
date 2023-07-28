#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
perc_tip = float(input("What percentage of tip would you like to give 10, 12 or 15 ? "))
No_to_split = int(input("How many people to split the bill? "))
pay_each = (total_bill*(perc_tip/100 + 1))/(No_to_split)
round_pay_each = round(pay_each, 2)
print(f"Each person should pay ${round_pay_each}: ")