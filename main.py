from python_intermediate.add_module import add
from python_intermediate.sub_module import subtract

print("Addition:",add(19,60));
print("Subtraction:",subtract(19,6))

try:
  x=10/0;
except ZeroDivisionError:
  print("You cannot divide by zero!")

try:
    num = int("abc")   # ValueError
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid number")

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", x)
