def parse_input():
  d = {}
  for line in open('2.txt').readlines():
    line = line.strip()
    l = line.split(': ')[0]
    r = line.split(': ')[1]
    ID = int(l.replace('Game ', ''))
    d[ID] = []
    for sh in r.split('; '):
      t = dict()
      for pair in sh.split(', '):
        n = pair.split(' ')[0]
        c = pair.split(' ')[1]
        t[c] = int(n)
      d[ID].append(t)
  return d

def first_part(inp):
  res = 0
  for k, v in inp.items():
    flag = True
    for d in v:
      if d.get('red', 0) > 12 or d.get('green', 0) > 13 or d.get('blue', 0) > 14:
        flag = False
        break
    if flag:
      res += k
  return res

def second_part(inp):
  res = 0
  for k, v in inp.items():
    min_reds = [0]
    min_greens = [0]
    min_blues = [0]

    for d in v:
      min_reds.append(d.get('red', 0))
      min_greens.append(d.get('green', 0))
      min_blues.append(d.get('blue', 0))
    res += max(min_reds) * max(min_greens) * max(min_blues)
  return res

inp = parse_input()
print('First part:', first_part(inp))
print('Second part:', second_part(inp))
