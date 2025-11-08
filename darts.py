'''
f the dart lands outside the target, player earns no points (0 points).
If the dart lands in the outer circle of the target, player earns 1 point.
If the dart lands in the middle circle of the target, player earns 5 points.
If the dart lands in the inner circle of the target, player earns 10 points.
The outer circle has a radius of 10 units (this is equivalent to the total radius for the entire target),
the middle circle a radius of 5 units, and the inner circle a radius of 1.
Of course, they are all centered at the same point — that is, the circles are concentric defined by the coordinates (0, 0).
'''

def score(x, y):
    # print(9 ** (0.5))
    if x < 0:
        x = abs(x)
    if y < 0:
        y = abs(y)

    if x != 0 and y != 0:
        radius = ((x ** 2 + y ** 2) ** 0.5)
    if x == 0:
        radius = y
    if y == 0:
        radius = x
    
    if radius > 10:
        return 0
    if radius <= 10 and radius > 5:
        return 1
    if radius <= 5 and radius > 1:
        return 5
    if radius <= 1:
        return 10
    

#r = score(-5,0)
#print(r)
#r = score(0.7, 0.7)
#print(r)
r = score(-5,0)
print(r)
#r = score(0, 0)
#print(r)