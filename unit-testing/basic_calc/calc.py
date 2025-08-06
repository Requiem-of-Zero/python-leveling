# Add Function
def add(x, y):
  return x+y

# Subtract Function
def subtract(x, y):
  return x-y

# Multiply Function
def multiply(x, y):
  return x*y

# Divide Function
def divide(x, y):
  if y == 0:
    raise ValueError("Cannot divide by zero")
  return x/y