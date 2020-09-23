import math

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
                list_dummy.append((x-y)*(x-y))
    else:
        return 0
    mse_value = summation(list_dummy)/len(list_dummy)
    mse_value = round(mse_value, 3)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    list_dummy = []
    if len(first_list) == len(second_list):
        for x, y in zip(first_list, second_list):
            if type(x) == type("s") or type(y) == type("s"):
                return 0
            else:
                list_dummy.append(abs(x-y))
    else:
        return 0
    mae_value = summation(list_dummy)/len(list_dummy)
    mae_value = round(mae_value, 3)

    return mae_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    if mse(first_list, second_list) > 0:
        rmse_value = math.sqrt(mse(first_list, second_list))
    else:
        return 0
    return rmse_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    list_dummy = []
    m = mean(first_list)
    for x, y in zip(first_list, second_list):
        if type(x) == type("s") or type(y) == type("s"):
            return 0
        else:
            list_dummy.append(m)

    if mse(first_list, list_dummy) == 0:
        return 0
    else:
        nse_value = 1-(mse(first_list, second_list) /
                       mse(first_list, list_dummy))
    nse_value = round(nse_value, 2)
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    list1 = []
    list2 = []
    list3 = []
    if len(first_list) == len(second_list):
        for x, y in zip(first_list, second_list):
            m = mean(first_list)
            n = mean(second_list)
            if type(x) == type("s") or type(y) == type("s"):
                return 0
            else:
                list1.append((x-m)*(y-n))
                list2.append((x-m)*(x-m))
                list3.append((y-n)*(y-n))
    else:
        return 0
    pcc_value = summation(list1)/math.sqrt(summation(list2)*summation(list3))
    pcc_value = round(pcc_value, 3)
    return pcc_value


def sorting(first_list):
    n = len(first_list)

    for x in first_list:
        if type(x) == type("s"):
            return 0
        else:
            for i in range(n-1):
                for j in range(0, n-i-1):
                    if first_list[j] > first_list[j+1]:
                        first_list[j], first_list[j +
                                                  1] = first_list[j+1], first_list[j]
    sorted_list = first_list
    return sorted_list


def variance(first_list):
    list_dummy = []
    m = mean(first_list)
    for x in first_list:
        if type(x) == type("s"):
            return 0
        else:
            list_dummy.append((x-m)*(x-m))
    variance_value = summation(list_dummy)/len(first_list)
    variance_value = round(variance_value, 3)
    return variance_value


# Function to compute median. You cant use Python functions
def median(first_list):
    n = len(first_list)
    sorted_list = sorting(first_list)

    if n % 2 == 0:
        median_value = (sorted_list[int(n/2)]+sorted_list[int(n/2)-1])/2
    else:
        median_value = sorted_list[(n-1)/2]

    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    standard_deviation_value = math.sqrt(variance(first_list))
    standard_deviation_value = round(standard_deviation_value, 3)
    return standard_deviation_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    list_dummy = []
    for x in first_list:
        if type(x) == type("s"):
            return 0
        else:
            m = mean(first_list)
            var = variance(first_list)
            sk = (x-m)/var
            list_dummy.append(sk*sk*sk)

    skewness_value = summation(list_dummy)/len(first_list)
    skewness_value = round(skewness_value, 3)

    return skewness_value


list1 = [1, 26,  4]
print(skewness(list1))
