inp = [x for x in open('inp5.txt').readlines()]
lines = []
not_diagonal_lines = []
for line in inp:
  tmp = line.split(' -> ')
  x1, y1 = [int(x) for x in tmp[0].split(',')]
  x2, y2 = [int(x) for x in tmp[1].split(',')]
  lines.append([x1, y1, x2, y2])
  if x1 == x2 or y1 == y2:
    not_diagonal_lines.append([x1, y1, x2, y2])

def overlap_count(lines):
  diagram = []
  for i in range(1000):
    diagram.append([None] * 1000)
  for i in range(len(lines)):
    x1, y1, x2, y2 = lines[i]
    if x1 == x2:
      for k in range(min(y1, y2), max(y1, y2) + 1):
        if diagram[k][x1] == None:
          diagram[k][x1] = 1
        else:
          diagram[k][x1] += 1
    elif y1 == y2:
      for k in range(min(x1, x2), max(x1, x2) + 1):
        if diagram[y1][k] == None:
          diagram[y1][k] = 1
        else:
          diagram[y1][k] += 1
    else:
      x_add = 1 if x2 > x1 else -1
      y_add = 1 if y2 > y1 else -1
      start_coord = [x1, y1]
      end_coord = [x2 + x_add, y2 + y_add]
      k = 0
      while start_coord[0] + k * x_add != end_coord[0]:
        cell = diagram[start_coord[1] + k * y_add][start_coord[0] + k * x_add]
        if cell == None:
          diagram[start_coord[1] + k * y_add][start_coord[0] + k * x_add] = 1 
        else:
          diagram[start_coord[1] + k * y_add][start_coord[0] + k * x_add] += 1
        k += 1

  cnt = 0
  for x in diagram:
    for y in x:
      if y and y >= 2:
        cnt += 1
  return cnt

print('First part:', overlap_count(not_diagonal_lines))
print('Second part:', overlap_count(lines))
