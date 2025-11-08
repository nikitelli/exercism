resistors = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def value(colors):
    code = ''
    count_colors = len(colors)
    if count_colors == 2:
        for item in colors:
            value = resistors[item]
            code = str(code) + str(value)
    if count_colors == 3:
        colors.pop()
        for item in colors:
            value = resistors[item]
            code = str(code) + str(value)
            
    return code

#r = value(["brown", "black"])
#print(r)
r = value(["green", "brown", "orange"])
print(r)