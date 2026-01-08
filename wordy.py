import re

# equation is a list that will hold the parsed elements of the equation, eg. ['3', 'plus', '2', 'multiplied', 'by', '3']
equation = []
thisdict = {
    "plus": "+",
    "minus": "-",
    "multiplied": "*",
    "divided": "/"
}

def answer(text):
    if text == "":
        return "syntax error!!"

    if len(text) > 0:
        match = re.search(r"\d+.+\d+\^?", text)
        if match is not None:
            matched = match.group()
            equation = matched.split()
            print(equation)
        elif match is None:
            return "syntax error!!"            
        else:
            return "syntax error!!"

        for x in equation:
            if x == "plus":
                index = equation.index(x)
                if (equation[index - 1]) == "+":
                    return "syntax error!"
                else:
                    operator = thisdict.get(x)
                    equation[index] = operator
            if x == "minus":
                index = equation.index(x)
                if (equation[index - 1]) == "-":
                    return "syntax error!"
                else:
                    operator = thisdict.get(x)
                    equation[index] = operator
            if x == "multiplied":
                operator = thisdict.get(x)
                index = equation.index(x)
                equation[index] = operator
                equation.pop(index + 1)
            if x == "divided":
                operator = thisdict.get(x)
                index = equation.index(x)
                equation[index] = operator
                equation.pop(index + 1)                

        # print(equation)
        expression = equation
        return eval(''.join(expression))


e = answer("What is 3 plus 2 multiplied by 3?")
print(e)
# e = answer("What is 5?")
# print(e)

# ------------
# e = answer("What is 52 cubed?")
# print(e)
# e = answer("")
# print(e)
# e = answer("What is 5 plus 13?")
# print(e)
# e = answer("What is 7 minus 5?")
# print(e)
# e = answer("What is 6 multiplied by 4?")
# print(e)
# e = answer("What is 25 divided by 5?")
# print(e)
# e = answer("What is 5 plus 13 plus 6?")
# print(e)
# e = answer("Who is the President of the United States")
# print(e)
