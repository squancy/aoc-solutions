f = open('inp3.txt').readlines()
rn = len(f)
rl = len(f[0].lstrip().rstrip())

def num_of_trees(right, down):
  m = int(rn / rl * right) + 1
  lines = []
  for line in f:
    line = line.lstrip().rstrip()
    lines.append(line * m)

  h = 0
  cnt = 0
  for i in range(0, rn, down):
    if lines[i][h] == '#':
      cnt += 1
    h += right
  return cnt

print('First part:', num_of_trees(3, 1))

cnt = 1
for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
  cnt *= num_of_trees(r, d)
print('Second part:', cnt)
