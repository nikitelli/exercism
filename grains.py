def square(number):
  max = 64
  for total_wheat in range(0,max):
    try:
      total_wheat =+ 2**total_wheat
      print(total_wheat)
    except Exception as err:
      raise ValueError("square must be between 1 and 64")


  return total_wheat

def total():
  total_wheat = square(64)
  print(total_wheat)

total()