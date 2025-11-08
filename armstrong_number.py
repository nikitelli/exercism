def is_armstrong_number(number):

  '''
  9 is an Armstrong number, because 9 = 9^1 = 9
  10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
  153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
  154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
  '''

  no_of_digits = len(str(number))
  liste = [int(x) for x in str(number)]
  sum = 0
  for i in liste:
    sum += i ** no_of_digits

  if sum == number:
    return True
  
  return False


bool = is_armstrong_number(154)
print(bool)