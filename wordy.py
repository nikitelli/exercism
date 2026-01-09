import re

# equation is a list that will hold the parsed elements of the equation, eg. ['3', 'plus', '2', 'multiplied', 'by', '3']
equation = []

# simple mapping from word operators to Python operator symbols
thisdict = {
    "plus": "+",
    "minus": "-",
    "multiplied": "*",
    "divided": "/"
}

def answer(text):
    # Return a syntax error for empty input quickly
    if text == "":
        return "syntax error!!"

    # Only try to parse non-empty inputs
    if len(text) > 0:
        # Use a regex to capture a simple pattern: number ... number (optionally ending with a ?)
        # This is a very permissive match; it will capture the numeric parts and intervening words.
        match = re.search(r"\d+.+\d+\^?", text)
        if match is not None:
            # Extract the matched substring and split on whitespace to get tokens
            matched = match.group()
            equation = matched.split()
            print(equation)  # debug print showing the parsed token list
        elif match is None:
            # If regex didn't match, the input is not in an expected format
            return "syntax error!!"            
        else:
            # Defensive fallback (unreachable because above covers both cases)
            return "syntax error!!"

        # Iterate over tokens and replace word operators with symbols
        # Also handle the 'by' token that follows 'multiplied'/'divided' by removing it
        for x in equation:
            if x == "plus":
                index = equation.index(x)
                # Check for consecutive operator tokens (very basic validation)
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
                # 'multiplied by' should map to '*' and remove the 'by' token
                operator = thisdict.get(x)
                index = equation.index(x)
                equation[index] = operator
                equation.pop(index + 1)
            if x == "divided":
                # 'divided by' should map to '/' and remove the 'by' token
                operator = thisdict.get(x)
                index = equation.index(x)
                equation[index] = operator
                equation.pop(index + 1)                

        # Join the token list into a single expression string and evaluate it.
        # Note: using eval on constructed strings can be unsafe in other contexts.
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
