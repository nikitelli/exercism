import string

def is_valid(isbn):

  lower_chars = string.ascii_lowercase
  upper_chars = string.ascii_uppercase

  result = 0

  if len(isbn) != 13:
    return False
  
  for char in isbn:
    if char in lower_chars:
      return False

  dig10 = ''
  for char in isbn:
    if char in upper_chars:
      if char == 'X' and isbn[12] == 'X':
        dig10 = 10
      else:
        print('YY')
        return False

  if dig10 != 10:
    dig10 = int(isbn[12])

  print('DIG10: ' + str(dig10))

  # if any(char in lower_chars for char in isbn):
  #   return False
  # if any(char in upper_chars for char in isbn):
  #     if isbn[12] == 'X':
  #       dig10 = 10
  # else:
  #   return False
  
  dig1 = int(isbn[0])
  dig2 = int(isbn[2])
  dig3 = int(isbn[3])
  dig4 = int(isbn[4])
  dig5 = int(isbn[6])
  dig6 = int(isbn[7])
  dig7 = int(isbn[8])
  dig8 = int(isbn[9])
  dig9 = int(isbn[10])

  # dig1 = isbn[0]
  # dig2 = isbn[2]
  # dig3 = isbn[3]
  # dig4 = isbn[4]
  # dig5 = isbn[6]
  # dig6 = isbn[7]
  # dig7 = isbn[8]
  # dig8 = isbn[9]
  # dig9 = isbn[10]

  #print(type(dig10))
  
  result = (dig1 * 10 + dig2 * 9 + dig3 * 8 + dig4 * 7 + dig5 * 6 + dig6 * 5 + dig7 * 4 + dig8 * 3 + dig9 * 2 + dig10) % 11
  #result = (int(dig1) * 10 + int(dig2) * 9 + int(dig3) * 8 + int(dig4) * 7 + int(dig5) * 6 + int(dig6) * 5 + int(dig7) * 4 + int(dig8) * 3 + int(dig9) * 2 + dig10) % 11
  #result = 0
  if result == 0:
    return True
  else:
    return False
    
r = is_valid("3598215088")
print(r)