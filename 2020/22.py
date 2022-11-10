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

def manage_cards(p1, p2):
  if p1[0] > p2[0]:
    p1 = p1[1:] + [p1[0], p2[0]]
    p2 = p2[1:]
  else:
    p2 = p2[1:] + [p2[0], p1[0]]
    p1 = p1[1:]
  return p1, p2

def recursive_combat(p1, p2):
  prev_games = []
  while True:
    prev_games.append([p1, p2])
    if len(p1) == 0:
      return [2, p2]
    elif len(p2) == 0:
      return [1, p1]
    elif [p1, p2] in prev_games[:-1]:
      return [1, p1]
    elif len(p1) - 1 >= p1[0] and len(p2) - 1 >= p2[0]:
      winner = recursive_combat(p1[1:p1[0] + 1], p2[1:p2[0] + 1])
      if winner[0] == 1:
        p1 = p1[1:] + [p1[0], p2[0]]
        p2 = p2[1:]           
      else:
        p2 = p2[1:] + [p2[0], p1[0]]
        p1 = p1[1:]
    else:
      p1, p2 = manage_cards(p1, p2)

def second_part(p1, p2):
  a, b = recursive_combat(p1, p2)
  return calc_score(b)

print('First part:', first_part(p1, p2))
print('Second part:', second_part(p1, p2))
