arr = [list(x.lstrip().rstrip()) for x in open('inp25.txt').readlines()]

def next_index(cucumber_type, i, j, arr):
  if cucumber_type == '>':
    if j < len(arr[i]) - 1 and arr[i][j + 1] == '.':
      return (i, j + 1)
    elif j == len(arr[i]) - 1 and arr[i][0] == '.':
      return (i, 0)
  else:
    if i < len(arr) - 1 and arr[i + 1][j] == '.':
      return (i + 1, j)
    elif i == len(arr) - 1 and arr[0][j] == '.':
      return (0, j)
  return None

def move_cucumber(d, c, arr):
  moved = False
  arr = [[x for x in y] for y in arr]
  for from_pos in d:
    to_pos = d[from_pos]
    arr[from_pos[0]][from_pos[1]] = '.'
    arr[to_pos[0]][to_pos[1]] = c
    moved = True
  return (arr, moved)

def simulate_step(arr):
  # first simulate east moves
  arr = [[x for x in y] for y in arr]
  east_moves = {}
  changed_east = False
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      ni_east = next_index('>', i, j, arr)
      if arr[i][j] == '>' and ni_east != None:
        east_moves[(i, j)] = ni_east

  arr, changed_east = move_cucumber(east_moves, '>', arr)
  
  # then simulate south moves
  south_moves = {}
  changed_south = False
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      ni_south = next_index('v', i, j, arr)
      if arr[i][j] == 'v' and ni_south != None:
        south_moves[(i, j)] = ni_south

  arr, changed_south = move_cucumber(south_moves, 'v', arr)
  
  return (arr, changed_east or changed_south)

changed = True
steps = 0
while changed:
  arr, changed = simulate_step(arr)
  """
  for row in arr:
    print(''.join(row))
  print()
  """
  steps += 1
print(steps)
