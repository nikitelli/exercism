resistors = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def value(colors):
    code = ''
    max_value = 1
    last_digit = 0
    for item in colors:
        value = str(resistors[item])
        print('value: ' + value)
        if max_value == 3:
            last_digit = 10 ** int(value)
            print('last_digit: ' +str(last_digit))
        else:
            code = code + value
        max_value += 1

    code = int(code) * last_digit

    if last_digit >= 0 and last_digit == 100:
        code_str = str(code) + ' ohms'
    if last_digit == 1000:
        code = code / 1000
        code_str = str(code) + ' kiloohms'
    return code_str

def label(colors):
    return value(colors)

#             5        1        3    -> 51000
# r = label(["green", "brown", "orange"])
# print('result: ' + str(r))

#               3         3         0  -> 33
# r = label(["orange", "orange", "black"])
# print('result: ' + str(r))

#            2       0       2     -> 2 kiloohms
r = label(["red", "black", "red"])
print('result: ' + str(r))
