# Function to compute sum. You cant use Python functions
def summation(first_list):
    summation_value = 0
    for x in first_list:
        if type(x) == type("s"):
            return 0
        else:
            summation_value += x
            summation_value = round(summation_value, 3)
    return summation_value
