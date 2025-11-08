import re

def is_paired(input_string):
    replaced = re.sub(r"[^\[\(\{\}\)\]]|\{\}|\(\)|\[\]", "", input_string)
    if input_string == replaced:
        return not input_string
    else:
        is_paired(replaced)
    #return not input_string if input_string == replaced else is_paired(replaced)

p = is_paired("[[")
print(p)