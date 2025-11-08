'''
To shift a letter, you'll need to convert it to a numerical value, perform the shift, and then convert it back to a letter.
The built-in functions ord() and chr() are perfect for this.

ord(character) returns the Unicode code point of a character.

chr(integer) returns the character represented by the given Unicode code point.

For example, ord('a') is 97 and ord('b') is 98. By using these, you can shift a letter by adding the key to its ordinal value.
----
To handle both uppercase and lowercase letters correctly, you'll need to manage the character ranges separately.
You can use the isupper() and islower() methods you identified earlier.
----
The most crucial part of the algorithm is handling the wraparound. When a letter is shifted past Z (or z), it should "wrap around"
to the beginning of the alphabet. This is a classic modular arithmetic problem. The modulo operator (%) is the key here.
The general formula for a rotational cipher on the alphabet is:

new_ord = (ord(char) - base_ord + key) % 26 + base_ord

Where base_ord is the starting Unicode code point for the alphabet (ord('a') for lowercase, ord('A') for uppercase).
By subtracting the base before applying the modulo, you effectively normalize the range to 0-25. After the calculation,
you add the base back to get the correct new character.
'''

def rotate(text, key):
    base_ord_low = ord('a')
    base_ord_up = ord('A')
    new_cipher_string = ''
    for x in text:
        if x.isalpha():
            if x.islower():
                unicode = ord(x)
                new_ord = (unicode - base_ord_low + key) % 26 + base_ord_low
                #print(new_ord)
                new_letter = chr(new_ord)
                #print(new_letter)
                new_cipher_string += new_letter
            if x.isupper():
                unicode = ord(x)
                new_ord = (unicode - base_ord_up + key) % 26 + base_ord_up
                #print(new_ord)
                new_letter = chr(new_ord)
                #print(new_letter)
                new_cipher_string += new_letter
        else:
            new_cipher_string += x

    return new_cipher_string


s = rotate('a', 0)
print(s)
s = rotate('OMG', 5)
print(s)
s = rotate('Testing 1 2 3 testing', 4)
print(s)
s = rotate("Let's eat, Grandma!", 21)
print(s)
s = rotate("The quick brown fox jumps over the lazy dog.", 13)
print(s)