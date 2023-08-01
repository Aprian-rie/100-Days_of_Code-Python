def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2
 
operations = {"+": add,
              "-": subtract,
              "*":multiply,
              "/": divide
             }
num1 = int(input("What's the first number: "))
for op in operations:
  print(op)
op_symbol = input("Pick an operation from the one's above: ")
num2 = int(input("What's the second number: "))
calculation_function = operations[op_symbol]
first_answer = calculation_function(num1, num2)
print(f"{num1} {op_symbol} {num2} = {first_answer}")

num3 = int(input("What's the next number: "))
op_symbol = input("Next operation: ")
calculation_function_two = operations[op_symbol]
second_answer = calculation_function_two(first_answer, num3)
print(f"{first_answer} {op_symbol} {num3} = {second_answer}")
