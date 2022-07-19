import math

def calc_variance(values):
    mean = sum(values)/len(values)

    additive = 0
    for i in values:
        additive += (i-mean)**2

    variance = additive/(len(values) - 1)

    return variance

def find_median(values):
    len_list = len(values)
    if len_list % 2 == 0:
        half = int(len_list / 2)
        median = (values[half - 1] + values[half])/2
    else:
        half = math.floor(len_list/2)
        median = values[half]

    return (half, median)

def calculate_quartiles(values):
    values = sorted(values)
    list_len = len(values)
    lower_half = []
    upper_half = []
    if list_len % 2 == 0:
        median = find_median(values)
        lower_half = values[0:median[0]]
        upper_half = values[median[0]:]
    else:
        median = find_median(values)
        lower_half = values[0:median[0]]
        upper_half = values[median[0] + 1:]

    first_quartile = find_median(lower_half)
    third_quartile = find_median(upper_half)
    iqr = third_quartile[1] - first_quartile[1]


    return {
            'min': values[0],
            'first quartile': first_quartile[1],
            'second quartile (median)': median[1],
            'third quartile': third_quartile[1],
            'max': values[-1],
            'IQR': iqr
            }

def calc_statistical_values(values):
    ordered = sorted(values)
    mean = sum(values)/len(values)
    variance = calc_variance(values)
    standard_deviation = math.sqrt(variance)
    quartiles = calculate_quartiles(values)

    return{'ordered_list': ordered,
            'mean' : mean,
            'variance': variance,
            'SD': standard_deviation,
            'quartiles': quartiles}


# Input any list of numbers here
values = [1, 1, 2, 4, 4, 5] 

data = calc_statistical_values(values)

for k, v in data.items():
    print(k,':', v)
