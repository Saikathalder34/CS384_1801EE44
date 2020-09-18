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


# function for power
def power(num1, num2):
    x = 1
    power = 1
    if type(num1) != type("c") and type(num2) == type(1):
        while x <= abs(num2):
            power *= num1
            x += 1
    else:
        return 0
    if num2 <= 0:
        return 1/power
    return power


# function for GP
def printGP(a, r, n):
    gp = []
    x = 0
    if type(a) != type("c") and type(r) != type("c") and type(n) == type(1):
        while(x < n):
            gp.append(round(a*power(r, x), 3))
            x += 1
    else:
        gp.append(0)
    return gp
