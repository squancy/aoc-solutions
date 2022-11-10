lines = [x.rstrip() for x in open('inp24.txt').readlines()]

def parse_line(line):
  res = []
  i = 0
  while i < len(line):
    if line[i] in ['e', 'w']:
      res.append(line[i])
      i += 1
    elif line[i:i + 2] in ['se', 'sw', 'nw', 'ne']:
      res.append(line[i:i + 2])
      i += 2
  return res

def move_dir(d, pos):
  if d == 'e':
    pos = [pos[0] - 2, pos[1]]
  elif d == 'se':
    pos = [pos[0] - 1, pos[1] - 1]
  elif d == 'sw':
    pos = [pos[0] + 1, pos[1] - 1]
  elif d == 'w':
    pos = [pos[0] + 2, pos[1]]
  elif d == 'nw':
    pos = [pos[0] + 1, pos[1] + 1]
  elif d == 'ne':
    pos = [pos[0] - 1, pos[1] + 1]
  return pos

def first_part(lines):
  blacks = []
  for line in lines:
    directions = parse_line(line) 
    pos = [0, 0]
    for d in directions:
      pos = move_dir(d, pos)
    if pos in blacks:
      blacks.remove(pos)
    else:
      blacks.append(pos)
  return [len(blacks), blacks]

def get_neighbors(cur_pos):
  return [
    (cur_pos[0] + 2, cur_pos[1]),
    (cur_pos[0] + 1, cur_pos[1] + 1),
    (cur_pos[0] - 1, cur_pos[1] + 1),
    (cur_pos[0] - 2, cur_pos[1]),
    (cur_pos[0] - 1, cur_pos[1] - 1),
    (cur_pos[0] + 1, cur_pos[1] - 1)
  ]

def num_of_adj_blacks(blacks, nbs):
  cnt = 0
  for nb in nbs:
    if nb in blacks:
      cnt += 1
  return cnt

def day(blacks):
  blacks_next = {}
  for k, v in blacks.items(): blacks_next[k] = v
  
  for bt in blacks.keys():
    nbs = get_neighbors(bt)
    cnt = num_of_adj_blacks(blacks, nbs)
    if cnt == 0 or cnt > 2:
      del blacks_next[bt]
    whites = [x for x in nbs if not x in blacks]
    for wt in whites:
      nbs_w = get_neighbors(wt)
      cnt_w = num_of_adj_blacks(blacks, nbs_w)
      if cnt_w == 2 and not wt in blacks_next:
        blacks_next[wt] = 1 
  return blacks_next

def second_part(blacks):
  for i in range(100):
    blacks = day(blacks) 
  return len(blacks)

res, blacks = first_part(lines)
d = {}
for (x, y) in blacks: d[(x, y)] = 1 # use a dict for better performance
print('First part:', res)
print('Second part:', second_part(d))
