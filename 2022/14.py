import copy

rocks = {}

for line in open('14.txt').readlines():
  line = [[int(y) for y in x.split(',')] for x in line.strip().split(' -> ')]
  for i in range(1, len(line)):
    curX, prevX = line[i][0], line[i - 1][0]
    curY, prevY = line[i][1], line[i - 1][1]
    if curX == prevX:
      for j in range(min(curY, prevY), max(curY, prevY) + 1):
        rocks[(curX, j)] = 1 
    else:
      for j in range(min(curX, prevX), max(curX, prevX) + 1):
        rocks[(j, curY)] = 1

LOWEST_Y = max([x[1] for x in rocks.keys()])
FLOOR_Y = LOWEST_Y + 2
SS = [500, 0]

def gen_pos(spos):
  return [
      (spos[0], spos[1] + 1),
      (spos[0] - 1, spos[1] + 1),
      (spos[0] + 1, spos[1] + 1)
  ]

def get_pos(spos, blocked, below, diag_left, diag_right):
  if not below in blocked:
    return below
  elif not diag_left in blocked:
    return diag_left
  elif not diag_right in blocked:
    return diag_right  
  return spos

def first_part(blocked, lowest_y):
  cnt = 0
  while True:
    spos = [500, 0]
    while True:
      below, diag_left, diag_right = gen_pos(spos)
      if spos[1] > lowest_y:
        return cnt
      new_spos = get_pos(spos, blocked, below, diag_left, diag_right)
      if new_spos != spos:
        spos = new_spos
      else:
        break
    blocked[tuple(spos)] = 1
    cnt += 1

def second_part(blocked, floor_y, ss):
  cnt = 0
  while True:
    spos = [500, 0]
    while True:
      below, diag_left, diag_right = gen_pos(spos)
      if ((ss[0], ss[1] + 1) in blocked and (ss[0] - 1, ss[1] + 1) in blocked
        and (ss[0] + 1, ss[1] + 1) in blocked):
        return cnt
      elif spos[1] == floor_y - 1:
        break
      new_spos = get_pos(spos, blocked, below, diag_left, diag_right)
      if new_spos != spos:
        spos = new_spos
      else:
        break
    blocked[tuple(spos)] = 1
    cnt += 1

rocks_copy = copy.deepcopy(rocks)
print('First part:', first_part(rocks, LOWEST_Y))
print('Second part:', second_part(rocks_copy, FLOOR_Y, SS) + 1)
