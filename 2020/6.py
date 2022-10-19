groups = []
f = open('inp6.txt').readlines()
tmp = []
for i in range(len(f)):
  line = f[i].lstrip().rstrip()
  if len(line) > 0:
    tmp.append(line)
  if len(line) == 0 or i == len(f) - 1:
    groups.extend([tmp])
    tmp = []

cnt = 0
for ans in groups:
  tr = ''
  for s in ans:
    tr += s
  cnt += len(set(tr))
print('First part:', cnt)

cnt = 0
for ans in groups:
  tr = set(ans[0])
  for i in range(1, len(ans)):
    tr &= set(ans[i])
  cnt += len(tr)
print('Second part:', cnt)
