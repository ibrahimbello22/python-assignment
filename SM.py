# Simple Calculator Program

# Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Display menu
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# User choice
choice = input("Choose operation (1/2/3/4): ")

# Input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operation
if choice == "1":
    result = add(num1, num2)
    print("Result =", result)

elif choice == "2":
    result = subtract(num1, num2)
    print("Result =", result)

elif choice == "3":
    result = multiply(num1, num2)
    print("Result =", result)

elif choice == "4":
    result = divide(num1, num2)
    print("Result =", result)

else:
    print("Invalid choice!")