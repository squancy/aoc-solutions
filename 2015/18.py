def parse_input():
  ons = {}
  s = 0
  for i, line in enumerate(open('inp18.txt').readlines()):
    s += 1
    line = line.strip()
    for j, c in enumerate(line):
      if c == '#':
        ons[(i, j)] = 1
  return ons, s

def num_nbs_on(i, j, ons, s):
  nbs_on = 0
  for x in range(i - 1, i + 2):
    for y in range(j - 1, j + 2):
      if x == i and y == j: continue
      if 0 <= x < s and 0 <= y < s and (x, y) in ons:
        nbs_on += 1
  return nbs_on
        

def simulate(s, ons, typ):
  if typ:
    new_ons = dict()
    new_ons[(0, 0)] = new_ons[(0, s - 1)] = new_ons[(s - 1, 0)] = new_ons[(s - 1, s - 1)] = 1
  else:
    new_ons = dict()
  for i in range(s):
    for j in range(s):
      if ((i, j) in ons and 2 <= num_nbs_on(i, j, ons, s) <= 3) or (not (i, j) in ons and num_nbs_on(i, j, ons, s) == 3):
        new_ons[(i, j)] = 1
  return new_ons 

def first_part():
  ons, s = parse_input()
  for i in range(100):
    ons = simulate(s, ons, False)
  return len(ons)

def second_part():
  ons, s = parse_input()
  ons[(0, 0)] = ons[(0, s - 1)] = ons[(s - 1, 0)] = ons[(s - 1, s - 1)] = 1
  for i in range(100):
    ons = simulate(s, ons, True)
  return len(ons) 

print('First part:', first_part())
print('Second part:', second_part())
