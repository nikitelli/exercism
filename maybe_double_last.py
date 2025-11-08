def maybe_double_last(hand):
  """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

  last_card = hand[-1]
  print(last_card)
  print(type(last_card))
  if last_card == 11:
    last_card = last_card * 2
    print(last_card)

  length = len(hand)
  new_list = hand[0:length-1:1]
  print(new_list)
  final_list = new_list + [last_card]
  return final_list

r = maybe_double_last([1, 2, 11])
print(r)