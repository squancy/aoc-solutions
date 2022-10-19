def calc_range(l, u, typ, inp):
  for c in inp:
    if c == typ:
      l, u = l, u - (u - l + 1) // 2
    else:
      l, u = l + (u - l + 1) // 2, u
  assert l == u
  return l

largest = 0
ids = []
for line in open('inp5.txt').readlines():
  line = line.lstrip().rstrip()
  row = line[:7]
  col = line[7:]
  r = calc_range(0, 127, 'F', row)
  c = calc_range(0, 7, 'L', col)
  sid = r * 8 + c
  ids.append(sid)
  if sid > largest:
    largest = sid

print('First part:', largest)
for i in range(len(ids) - 1):
  a = ids[i]
  for j in range(i + 1, len(ids)):
    b = ids[j]
    if a == b:
      continue
    if abs(a - b) == 2 and (min(a, b) + 1) not in ids:
      print('Second part:', min(a, b) + 1)
      break
