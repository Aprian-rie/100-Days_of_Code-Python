import art
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

def calculator():
  print(art.logo)
  num1 = float(input("What's the first number: "))
  for op in operations:
    print(op)
  to_continue = True
  while to_continue: 
    op_symbol = input("Pick an operation from the one's above: ")
    num2 = float(input("What's the next number: "))
    calculation_function = operations[op_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")
    user_continue = input((f"Type y to continue calculating with {answer} or type n to exit: "))
    if user_continue == 'n':
      to_continue = False
      calculator()
    elif user_continue == 'y':
      num1 = answer
calculator()
