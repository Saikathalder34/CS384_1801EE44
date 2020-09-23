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


# Function to compute mean
def mean(first_list):
    mean_value = summation(first_list)/len(first_list)
    mean_value = round(mean_value, 3)
    return mean_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    list_dummy = []
    if len(first_list) == len(second_list):
        for x, y in zip(first_list, second_list):
            if type(x) == type("s") or type(y) == type("s"):
                return 0
            else:
                list_dummy.append(x*x-y*y)

    else:
        return 0
    mse_value = summation(list_dummy)/len(list_dummy)
    mse_value = round(mse_value, 3)
    return mse_value
