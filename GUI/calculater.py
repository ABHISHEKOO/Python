# Define functions for basic operations
def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mul(x, y):
  return x * y

def div(x, y):
  if y == 0:
    return "Error! Division by zero is not allowed."
  else:
    return x / y

# Take user input
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform operation and display result
if op == "+":
  result = add(num1, num2)
  print("Result:", result)
elif op == "-":
  result = sub(num1, num2)
  print("Result:", result)
elif op == "*":
  result = mul(num1, num2)
  print("Result:", result)
elif op == "/":
  result = div(num1, num2)
  print("Result:", result)
else:
  print("Invalid operator!")
