# Constants for supported operations
# You will implement the functions add, subtract, multiply_op, and divide_op
# which take two numbers and return the result.
# Notice we don't use parentheses here. 
# We are storing the function itself, not the result of the function.
OPERATORS = {
    "plus": lambda a, b: a + b,
    "minus": lambda a, b: a - b,           # You'd define def subtract(a, b): return a - b
    "multiplied": lambda a, b: a * b,   # You'd define def multiply(a, b): return a * b
    "divided": lambda a, b: a // b
}

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply_op(a, b):
    return a * b

def divide_op(a, b):
    # Your division code here, remembering the result must be an integer!
    # Python's integer division (//) might be helpful.
    return a // b

def tokenize_problem(problem_string):
    # 1. Clean the string
    cleaned = problem_string.strip()
    if not (cleaned.startswith("What is ") and cleaned.endswith("?")):
        # Raise an error for non-standard questions
        raise ValueError("Invalid question format") 
        
    expression = cleaned[len("What is "):-1].strip()

    # 2. Standardize multi-word operations
    # Use a unique placeholder. This helps catch errors if 'by' is used elsewhere.
    expression = expression.replace(" multiplied by ", " multiplied ")
    expression = expression.replace(" divided by ", " divided ")

    # 3. Tokenize by spaces
    tokens = expression.split()
    
    # Check for empty input (e.g., "What is ?")
    if not tokens:
        raise ValueError("Empty question") 

    return tokens

def answer(question):
    tokens = tokenize_problem(question)
    
    # Iteration 0 & Initial Setup: The first token MUST be the starting number.
    try:
        # Initialize the accumulator with the first number
        accumulator = int(tokens[0])
    except ValueError:
        # Catches "Who is..." or "plus 5"
        raise ValueError("Invalid syntax or unsupported operation") 

    # Check for Iteration 0 completion ("What is 5?")
    if len(tokens) == 1:
        return accumulator

    # Iteration 3: Process the rest of the tokens in pairs (Operator, Number)
    i = 1 # Start checking from the second token (expected to be an operator)
    while i < len(tokens):
        # 1. Check for the Operator (at index i, which should be ODD)
        operator_word = tokens[i]
        
        # Check if the token is a recognized operator. This handles unsupported ops.
        if operator_word not in OPERATORS:
            # Handles "cubed" or "What is 5 plus 10 minus" (missing number after minus)
            raise ValueError("Invalid syntax or unsupported operation") 
            
        operation = OPERATORS[operator_word]

        # 2. Check for the Number (at index i + 1, which should be EVEN)
        # This handles tokens ending on an operator (e.g., "5 plus")
        if i + 1 >= len(tokens):
            raise ValueError("Invalid syntax: expression ends on an operator")
            
        operand_token = tokens[i+1]
        
        try:
            operand = int(operand_token)
        except ValueError:
            # Catches "plus plus" or "plus five" (if 'five' isn't handled)
            raise ValueError("Invalid syntax or unsupported operation") 

        # 3. Perform Left-to-Right Evaluation
        accumulator = operation(accumulator, operand)
        
        # Advance the index by 2 (to the next operator position)
        i += 2

    return accumulator

e = answer("What is 5 plus 13?")
print(e)
e = answer("What is 5?")
print(e)
e = answer("What is 6 multiplied by 4?")
print(e)
e = answer("What is 5?")
print(e)
e = answer("What is 52 cubed?")
print(e)
e = answer("")
print(e)
e = answer("What is 5 plus 13?")
print(e)
e = answer("What is 7 minus 5?")
print(e)
e = answer("What is 6 multiplied by 4?")
print(e)
e = answer("What is 25 divided by 5?")
print(e)
e = answer("What is 5 plus 13 plus 6?")
print(e)
e = answer("Who is the President of the United States")
print(e)