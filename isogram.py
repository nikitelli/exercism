import string

def is_isogram(string):

    #letters = 'abcdefghijklmnopqrstuvwxyz'
    #lower_chars = string.ascii_lowercase
    #upper_chars = string.ascii_uppercase

    liste = []
    for char in string:
        if char == '-' or char == ' ':
            continue
        if char.lower() not in liste:
            liste += char.lower()
        else:
            return False
    return True

r = is_isogram('alphAbet')
print(r)