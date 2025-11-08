def square_root(number):
    i = 1
    y = 1
    while i < 30:
        y = 0.5 * (y + number/y)
        i += 1

    return round(y)

sr = square_root(65025)
print(sr)