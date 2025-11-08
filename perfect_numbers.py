def classify(number):

    sum = 0
    try:
        for x in range(1,number):
            if number % x == 0:
                sum += x
        if sum == number:
            return "perfect"
        if sum > number:
            return "abundant"
        if sum < number:
            return "deficient"
    except:
        print("Exception occured")

r = classify(0)
print(r)