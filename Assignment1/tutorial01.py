# Function to add two numbers
def add(num1, num2):
    "This function perform addition"
    if type(num1) == type("s") or type(num2) == type("s"):
        return 0
    addition = num1 + num2
    return addition


# Function to subtract two numbers
def subtract(num1, num2):
    "This function perform subtraction"
    if type(num1) == type("s") or type(num2) == type("s"):
        return 0
    subtraction = num1 - num2
    return subtraction


# Function to multiply two numbers
def multiply(num1, num2):
    "This function perform multiplication"
    if type(num1) == type("s") or type(num2) == type("s"):
        return 0
    multiplication = num1*num2
    return multiplication


# Function to divide two numbers
def divide(num1, num2):
    "This function perform division"
    if type(num1) == type("s") or type(num2) == type("s"):
        return 0
    elif num1 and num2:
        division = num1/num2
    else:
        return 0
    return division
