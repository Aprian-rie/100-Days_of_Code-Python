#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
is_ordered = input("Would you like ordered or mixed (O or M) ?")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
combination_ordered = []
result_ordered = ''
result_mixed = ''
for number_letters in range(0,nr_letters):
  combination_ordered.append(letters[random.randint(0,51)])
for number_symbols in range(0,nr_symbols):
  combination_ordered.append(symbols[random.randint(0,8)])
for number_numbers in range(0,nr_numbers):
  combination_ordered.append(numbers[random.randint(0,9)])
for comb in combination_ordered:
  result_ordered += comb
#print(result_ordered)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
combination_mixed = random.sample(combination_ordered, len(combination_ordered))
for mixed_comb in combination_mixed:
  result_mixed += mixed_comb
#print(result_mixed)
if is_ordered == "O":
  print(result_ordered)
elif is_ordered == "M":
  print(result_mixed)
  ##You can use random.choice try it at July 30th 2023
