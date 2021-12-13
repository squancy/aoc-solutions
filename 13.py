"""
  The solution is pretty slow, takes several seconds to run since it builds an array with approx.
  1M elements
  It could be improved by focusing on only the few visible points and track only their movement when
  folding
"""

coords = [[int(x) for x in y.rstrip().lstrip().split(',')] for y in open('inp13.txt').readlines() if y[0].isdigit()]
folds = [[('x' if x.split(' ')[2][0] == 'x' else 'y'), int(x.split(' ')[2].split('=')[1])] for x in open('inp13.txt').readlines() if x.startswith('fold')]
max_x_coord = 0
max_y_coord = 0
for pair in coords:
  if pair[0] > max_x_coord:
    max_x_coord = pair[0]
  if pair[1] > max_y_coord:
    max_y_coord = pair[1]

paper = []
for i in range(max_y_coord + 1):
  tmp = []
  for j in range(max_x_coord + 1):
    if [j, i] in coords:
      tmp.append('#')
    else:
      tmp.append('.')
  paper.append(tmp)

for fold in folds:
  if fold[0] == 'x':
    fix_point = fold[1]
    for i in range(len(paper)):
      k = 1
      while fix_point + k < len(paper[i]) and fix_point - k >= 0:
        copy_cell = paper[i][fix_point + k]
        if copy_cell == '#':
          paper[i][fix_point - k] = copy_cell
        k += 1
    paper = [[y[j] for j in range(len(y)) if j < fix_point] for y in paper]
  else:
    fix_point = fold[1]
    for j in range(len(paper[0])):
      k = 1
      while fix_point + k < len(paper) and fix_point - k >= 0: 
        copy_cell = paper[fix_point + k][j]
        if copy_cell == '#':
          paper[fix_point - k][j] = copy_cell
        k += 1
    paper = [paper[i] for i in range(len(paper)) if i < fix_point]

for line in paper:
  print(''.join(line))

cnt = 0
for row in paper:
  for ch in row:
    if ch == '#':
      cnt += 1
print(cnt)
