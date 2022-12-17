import re

pairs = []
beacons = {}
C = 4 * 10 ** 6
p = re.compile('Sensor at x=((?:\+|\-|)\d+), y=((?:\+|\-|)\d+): closest beacon is at x=((?:\+|\-|)\d+), y=((?:\+|\-|)\d+)')
for line in open('15.txt').readlines():
  line = line.strip()
  m = re.match(p, line)
  pairs.append([
    [int(m.group(1)), int(m.group(2))],
    [int(m.group(3)), int(m.group(4))],
    abs(int(m.group(1)) - int(m.group(3))) + abs(int(m.group(2)) - int(m.group(4)))])
  beacons[(int(m.group(3)), int(m.group(4)))] = 1

def mdis(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def first_part(pairs, Y):
  ys = {}
  for pair in pairs:
    S, B, r = pair[0], pair[1], pair[2]
    if S[1] + r >= Y or S[1] - r <= Y:
      i = 0
      while mdis(S, [S[0] + i, Y]) <= r:
        if not (S[0] + i, Y) in beacons: ys[S[0] + i] = 1
        if not (S[0] - i, Y) in beacons: ys[S[0] - i] = 1
        i += 1
  return len(ys)

def hor(pairs, Y):
  intervals = []
  for pair in pairs:
    S, B, r = pair[0], pair[1], pair[2]
    if S[1] + r >= Y or S[1] - r <= Y:
      i = r - mdis(S, [S[0], Y])
      if i < 0: continue
      intervals.append([S[0] - i, S[0] + i])

  si = sorted(intervals)
  flag = False
  covered = si[0][1]
  for i in range(1, len(si)):
    if si[i][0] - 1 > covered:
      return True
    elif si[i][1] > covered:
      covered = si[i][1]
  return False

def second_part(pairs):
  x, y = None, None
  for i in range(0, C + 1):
    if hor(pairs, i):
      y = i
      break

  for i in range(0, C + 1):
    f = True
    for pair in pairs:
      if mdis(pair[0], (i, y)) <= pair[2]:
        f = False
        break
    if f:
      x = i
      break
  return x * C + y
 

print('First part:', first_part(pairs, C // 2))
print('Second part:', second_part(pairs))
