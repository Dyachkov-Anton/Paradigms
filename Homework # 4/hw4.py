x_data = [100, 104, 108, 103, 106]
y_data = [10, 14, 18, 203, 16]

# Вычисление среднего значения

def get_average(data):
    sum = 0
    for val in data:
        sum+=val
    return sum / len(data)

# вычисление разности от среднего

def get_defs(data, average):
    defs = []
    for val in data:
        defs.append(val-average)
    return defs

# вычисление квадратов разности от среднего

def get_square(defs):
    squares = []
    for num in defs:
        squares.append(num*num)
    return squares

# вычисление суммы квадратов разности от среднего

def get_square_sum(squares):
    squares_sum = 0
    for square in squares:
        squares_sum+=square
    return squares_sum

# Вычисление произведения разностей от среднего

def get_average_defs(x_defs, y_defs):
    average_defs = []
    for i in range(len(x_defs)):
        average_defs.append(x_defs[i] * y_defs[i])
    return average_defs

# Вычисление суммы произведений разностей от среднего

def get_average_defs_sum(average_defs):
    sum = 0
    for defs_sum in average_defs:
        sum+=defs_sum
    return sum

def pirson(x_data, y_data):

    # Вычисление среднего значения
    x_average = get_average(x_data)
    y_average = get_average(y_data)

    # вычисление разности от среднего
    x_average_defs = get_defs(x_data, x_average)
    y_average_defs = get_defs(y_data, y_average)

    # вычисление квадратов разности от среднего
    x_squares = get_square(x_average_defs)
    y_squares = get_square(y_average_defs)

    # вычисление суммы квадратов разности от среднего
    x_squares_sum = get_square_sum(x_squares)
    y_squares_sum = get_square_sum(y_squares)

    # Вычисление произведения разностей от среднего    
    defs_mult = get_average_defs(x_average_defs, y_average_defs)

    # Вычисление суммы произведений разностей от среднего
    defs_mult_sum = get_average_defs_sum(defs_mult)
    return defs_mult_sum / ((x_squares_sum * y_squares_sum)**0.5)

print(pirson (x_data, y_data))

