# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = False

def sublist(list_one, list_two):
    if list_one == list_two:
        if len(list_one) == 0 and len(list_two) == 0:
            print('same=[]')
            return True
        else:
            i = 0
            while i < len(list_one):
                if list_one[i] == list_two[i]:
                    i = i + 1
                    continue
                else:
                    return False
            return True
    if len(list_one) == 0 and len(list_two) >= 1:
        return SUBLIST
    if len(list_two) == 0 and len(list_one) >= 1:
        return SUPERLIST
    if list_one != list_two:
        print('unequal length!')
        return UNEQUAL

    
# p = sublist([], [1, 2, 3])
# print(p)
# p = sublist([],[])
# print(p)
# p = sublist([1,2,3],[1,2,3])
# print(p)
# p = sublist([1, 2, 3], [1, 2, 3, 4])
# print(p)
# p = sublist([1, 2, 3], [2, 3, 4])
# print(p)
p = sublist([], [1, 2, 3])
print(p)