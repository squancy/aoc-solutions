import functools

p1_pos, p2_pos = [int(x.split(':')[1].lstrip().rstrip()) for x in open('inp21.txt').readlines()]
p1_score, p2_score = 0, 0
die = 1
toggle = 0
rolls = 0

def calc_pos(pos, roll):
  if (pos + roll) % 10 == 0:
    return 10
  else:
    return (pos + roll) % 10

while p1_score < 1000 and p2_score < 1000:
  rolls += 3
  roll = 3 * die + 3
  if toggle == 0:
    p1_pos = calc_pos(p1_pos, roll)
    p1_score += p1_pos
    toggle = 1
  else:
    p2_pos = calc_pos(p2_pos, roll)
    p2_score += p2_pos
    toggle = 0
  die += 3

print('First part:', rolls * min(p1_score, p2_score))

steps = []
for i in range(1, 4):
  for j in range(1, 4):
    for k in range(1, 4):
      steps.append(i + j + k)

@functools.cache
def play(p1_score, p2_score, p1_pos, p2_pos, toggle):
  if p1_score >= 21:
    return [1, 0]
  if p2_score >= 21:
    return [0, 1]

  p1_wins = 0
  p2_wins = 0

  orig_p1_score = p1_score
  orig_p2_score = p2_score
  orig_p1_pos = p1_pos
  orig_p2_pos = p2_pos

  for s in steps:
    if toggle == 0:
      p1_score = orig_p1_score
      p1_pos = orig_p1_pos
      p1_pos = calc_pos(p1_pos, s)
      p1_score += p1_pos
      p1, p2 = play(p1_score, p2_score, p1_pos, p2_pos, not toggle)
    else:
      p2_score = orig_p2_score
      p2_pos = orig_p2_pos
      p2_pos = calc_pos(p2_pos, s)
      p2_score += p2_pos
      p1, p2 = play(p1_score, p2_score, p1_pos, p2_pos, not toggle)
    p1_wins += p1
    p2_wins += p2

  return [p1_wins, p2_wins]

p1_pos, p2_pos = [int(x.split(':')[1].lstrip().rstrip()) for x in open('inp21.txt').readlines()]
print('Second part:', max(play(0, 0, p1_pos, p2_pos, 0)))
