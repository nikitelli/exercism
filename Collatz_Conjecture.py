def steps(number):
    how_often = 0
    i = number

    if number <= 0:
      raise ValueError("Only positive integers are allowed")

    while i != 1:
        if i % 2 == 0:
            i //= 2  # Use integer division for efficiency and to keep 'i' as an integer
        else:
            i = 3 * i + 1 # Corrected Collatz rule: 3*n + 1
        how_often += 1

    return how_often

result = steps(1000000)
print(result)