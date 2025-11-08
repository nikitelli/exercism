plain = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'zyxwvutsrqponmlkjihgfedcba'

def encode(plain_text):
    plain_text_lowercase = plain_text.casefold()
    encoded_string = ''
    i = 1
    for char in plain_text_lowercase:
        if char.isspace():
            continue
        if char in ".,:;!$":
            continue
        if i > 5:
            encoded_string += ' '
            i = 1
        if char.isalpha():
            index = plain.index(char)
            encoded_char = cipher[index]
            encoded_string += encoded_char
            i += 1
        else:
            encoded_string += char
            i += 1            

    return encoded_string


def decode(ciphered_text):
    ciphered_text_lowercase = ciphered_text.casefold()
    decoded_string = ''
    for char in ciphered_text_lowercase:
        if char.isspace():
            continue
        if char.isalpha():        
            index = cipher.index(char)
            decoded_char = plain[index]
            decoded_string += decoded_char
        else:
            decoded_string += char

    return decoded_string

p = decode("gvhgr mt123 gvhgr mt")  # -> testing123testing
print(p)
# p = encode(".Testing1 2 3 testing")
# print(p)
# p = encode('mindblowingly')
# print(p)
# p = encode('test')
# print(p)
# p = decode('gvhg')
# print(p)
# p = encode('O M G')
# print(p)
