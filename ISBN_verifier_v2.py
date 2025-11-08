import re

def is_valid(isbn):

  digits = '0123456789'
  dig = [None] * 10

  # Using a list comprehension:
  dig1, dig2, dig3, dig4, dig5, dig6, dig7, dig8, dig9, dig10 = [0] * 10

  # Remove hyphens from the ISBN for easier access to digits
  isbn_digits_only = isbn.replace('-', '')
  print('isbn_digits_only: ' +isbn_digits_only)
  #pattern = r"^(\d)-*(?=\d{3}-*)(?=\d{3})\d*Z*$"
  #pattern = r"^(\d)-*\d{3}-*\d{5}-*\d*Z*$"

  pattern = r'^\d{9}[0-9Z]$'
  #result = re.search(pattern, isbn_digits_only)
  #print('result: ' +str(result))
  if re.match(pattern, isbn_digits_only):
    print(f"'{isbn}' matches the 9-digits + 1-char pattern.")

    # Remove hyphens from the ISBN for easier access to digits
    #isbn_digits_only = isbn.replace('-', '')
    #print(isbn_digits_only)

    for i in range(10):
      # We want to assign to dig_values[0] for the first digit, dig_values[1] for the second, etc.

      # Check if the character at the current index in isbn_digits_only is a digit
      if i < len(isbn_digits_only) and isbn_digits_only[i] in digits:
        #print('a: ' +str(int(isbn_digits_only[i])))
        dig[i] = int(isbn_digits_only[i])
     

    print(f"dig1 (first digit of ISBN): {dig[0]}")
    print(f"dig2 (second digit of ISBN): {dig[1]}")
    print(f"dig3 (tenth digit of ISBN): {dig[2]}")
    print(f"dig4 (tenth digit of ISBN): {dig[3]}")
    print(f"dig5 (tenth digit of ISBN): {dig[4]}")
    print(f"dig6 (tenth digit of ISBN): {dig[5]}")
    print(f"dig7 (tenth digit of ISBN): {dig[6]}")
    print(f"dig8 (tenth digit of ISBN): {dig[7]}")
    print(f"dig9 (tenth digit of ISBN): {dig[8]}")
    print(f"dig10 (tenth digit of ISBN): {dig[9]}")

    check = (dig1 * 10 + dig2 * 9 + dig3 * 8 + dig4 * 7 + dig5 * 6 + dig6 * 5 + dig7 * 4 + dig8 * 3 + dig9 * 2 + dig10 * 1) % 11
    print('check: ' +str(check))

  else:
    return False

  if check == 0:
    return True
  else:
    return False

r = is_valid('3-598-21507-X')
print(r)