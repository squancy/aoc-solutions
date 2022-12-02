inp = [x.replace(' ', '').rstrip() for x in open('2.txt').readlines()]

def first_part(inp):
  shape = {'X': 1, 'Y': 2, 'Z': 3}
  outcome = {'AY': 6, 'BZ': 6, 'CX': 6, 'AX': 3, 'BY': 3, 'CZ': 3}
  return sum([shape[l[1]] + outcome.get(l, 0) for l in inp])

def second_part(inp):
  outcome = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}
  return sum([outcome[l] for l in inp])

print('First part:', first_part(inp))
print('Second part:', second_part(inp))
