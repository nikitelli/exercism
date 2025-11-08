def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    length = len(hand)

    sum_even = sum(hand[1:length:2])
    even_avg = (sum(hand[1:length:2])) / len(hand[1:length:2])
    print(sum_even, even_avg)

    sum_odd = sum(hand[::2])
    print('sum_odd: ' + (str(sum_odd))) #korrekt
    odd_avg = (sum(hand[::2])) / len(hand[::2])
    print('odd_len:' + str(len(hand[::2])))
    print(sum_odd, odd_avg)

    if even_avg == odd_avg:
        return True
    return False

r = average_even_is_average_odd([5, 6, 8])
print(r)