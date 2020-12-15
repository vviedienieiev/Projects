import art

print(art.logo)
first_number = float(input("Print first number:\n"))
print("Available operationsis: + - * /")
operation = input("Pick an operation:\n")
second_number = float(input("Print second number:\n"))

def addition(l,r):
  return l+r

def substraction(l,r):
  return l-r

def multiplication(l,r):
  return l*r

def division(l,r):
  if r == 0:
    return 0
  else:
    return l/r

def calculate(l,r,operation):
  if operation == "+":
    return addition(l,r)
  elif operation == "-":
    return substraction(l,r)
  elif operation == "*":
    return multiplication(l,r)
  elif operation == "/":
    return division(l,r)

result = calculate(first_number,second_number,operation)
print(f"{first_number} {operation} {second_number} = {result}")
finish = False
while not finish:
  choice = input(f"Type 'y' to continue with {result}; type 'n' to start a new calculation; type 'c' to finish.").lower()
  if choice == 'n':
    first_number = float(input("Print first number:\n"))
    print("Available operationsis: + - * /\n")
    operation = input("Pick an operation:\n")
    second_number = float(input("Print second number:\n"))
    result = calculate(first_number,second_number,operation)
    print(f"{first_number} {operation} {second_number} = {result}")
  elif choice == 'y':
    first_number = result
    print("Available operationsis: + - * /\n")
    operation = input("Pick an operation:\n")
    second_number = float(input("Print second number:\n"))
    result = calculate(first_number,second_number,operation)
    print(f"{first_number} {operation} {second_number} = {result}")
  else:
    finish = True
