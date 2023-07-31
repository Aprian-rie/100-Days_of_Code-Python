# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
  print("Hello")
  print("How are you")
  print("fine")
greet()

#Function that allows input
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How are you {name}")
  print(f"You fine {name}")
greet_with_name("Apryan")

#Functions with more than one input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")
greet_with("Apryan", "Dodoma")
