p1 = []
p2 = []
toggle = 0

for line in open('inp22.txt').readlines():
  line = line.rstrip()
  if line == 'Player 1:':
    toggle = 0
    continue
  elif line == 'Player 2:':
    toggle = 1
    continue

  if not line:
    continue

  if toggle == 0:
    p1.append(int(line))
  else:
    p2.append(int(line))

def calc_score(p):
  return sum([p[::-1][i] * (i + 1) for i in range(len(p))])

def first_part(p1, p2):
  while True:
    if len(p1) == 0:
      return calc_score(p2)
    elif len(p2) == 0:
      return calc_score(p1)
    if p1[0] > p2[0]:
      p1 = p1[1:] + [p1[0], p2[0]]
      p2 = p2[1:]
    else:
      p2 = p2[1:] + [p2[0], p1[0]]
      p1 = p1[1:]

print('First part:', first_part(p1, p2))
