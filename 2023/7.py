import functools

def joker(card):
  d = {}
  for c in card:
    if c != 'J':
      if not c in d:
        d[c] = 1
      else:
        d[c] += 1
  if not d:
    return 'AAAAA'
  max_c = max(d, key=d.get)
  return card.replace('J', max_c)

def get_strength(card, is_first):
  if not is_first: 
    card = joker(card)
  a = list(set(card))
  if len(a) == 1:
    return 7
  elif len(a) == 2 and (card.count(a[0]) == 1 or card.count(a[0]) == 4) and ((card.count(a[1]) == 1 or card.count(a[1]) == 4)):
    return 6
  elif len(a) == 2 and (card.count(a[0]) == 2 or card.count(a[0]) == 3) and ((card.count(a[1]) == 2 or card.count(a[1]) == 3)):
    return 5
  elif len(a) == 3 and (card.count(a[0]) == 3 or card.count(a[1]) == 3 or card.count(a[2]) == 3):
    return 4
  elif len(a) == 3 and (card.count(a[0]) == 2 and card.count(a[1]) == 2) or (card.count(a[1]) == 2 and card.count(a[2]) == 2) or (card.count(a[0]) == 2 and card.count(a[2]) == 2):
    return 3
  elif len(a) == 4:
    return 2
  return 1

def get_stronger(a, b, A, is_first): 
  card1, card2 = a[0], b[0]
  s1, s2 = get_strength(card1, is_first), get_strength(card2, is_first)
  if s1 < s2:
    return -1 
  elif s1 > s2:
    return 1
  else:
    for i in range(len(card1)):
      if A.index(card1[i]) > A.index(card2[i]):
        return 1
      elif A.index(card1[i]) < A.index(card2[i]): 
        return -1

def solve(inp, A, is_first):
  cards = sorted(inp, key=functools.cmp_to_key(lambda a, b: get_stronger(a, b, A, is_first))) 
  return sum([(i + 1) * int(cards[i][1]) for i, x in enumerate(cards)])

A = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]
inp = [line.strip().split(' ') for line in open('7.txt').readlines()]
print('First part:', solve(inp, A, True))
A = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]
print('Second part:', solve(inp, A, False))
