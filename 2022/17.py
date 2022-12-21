jets = open('17.txt').readline().strip()

def rocks(y, ind):
  return [
    set([(2, y), (3, y), (4, y), (5, y)]),
    set([(3, y), (2, y + 1), (3, y + 1), (4, y + 1), (3, y + 2)]),
    set([(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)]),
    set([(2, y), (2, y + 1), (2, y + 2), (2, y + 3)]),
    set([(2, y), (3, y), (2, y + 1), (3, y + 1)])
  ][ind]

def first_part(jets, rind = 0, jind = 0, r = 2022):
  fixed_rocks = set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
  for i in range(r):
    h = max(y for (x, y) in fixed_rocks)
    cur_rock = rocks(h + 4, rind % 5) 
    t = 0
    while True:
      if not t and jets[jind % len(jets)] == '<' and min([x for (x, y) in cur_rock]) > 0:
        prop_cur_rock = set([(x - 1, y) for (x, y) in cur_rock])
        if len(prop_cur_rock & fixed_rocks) == 0:
          cur_rock = prop_cur_rock
        jind += 1
      elif not t and jets[jind % len(jets)] == '>' and max([x for (x, y) in cur_rock]) < 6:
        prop_cur_rock = set([(x + 1, y) for (x, y) in cur_rock])
        if len(prop_cur_rock & fixed_rocks) == 0:
          cur_rock = prop_cur_rock
        jind += 1
      elif not t:
        jind += 1
      else:
        prop_cur_rock = set([(x, y - 1) for (x, y) in cur_rock])
        if len(prop_cur_rock & fixed_rocks) > 0:
          break
        cur_rock = prop_cur_rock
      t = not t
    rind += 1
    fixed_rocks |= cur_rock

  return max(y for (x, y) in fixed_rocks)

def second_part(jets):
  # period = 1725
  # height of a period = 2709
  # period start = 2097
  # remaining to 1 trillion = 270
  # cycles until it becomes periodic = 1330 
  # index of rock = 1
  # pos in jet pattern = 7757

  """
  f = True
  yc = max(y for (x, y) in fixed_rocks)
  for xc in range(6):
    if not (xc, yc) in fixed_rocks:
      f = False
      break
  if f:
    print(yc, jind % len(jets), rind % 5, i)
  """

  x = (1000000000000 - 1330) // 1725
  r = (1000000000000 - 1330) % 1725
  return x * 2709 + 2097 + first_part(jets, 1, 7757, r) - 1

print('First part:', first_part(jets, 0, 0, 2022))
print('Second part:', second_part(jets))
