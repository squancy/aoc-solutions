import math

d = {}
cur_key = None
for line in open('inp20.txt'):
  line = line.rstrip()
  if line.startswith('Tile'):
    cur_key = int(line.split(' ')[1].replace(':', ''))
    d[cur_key] = []
  elif line:
    d[cur_key].append(line) 

def rotate(tile):
  new_tile = []
  for j in range(len(tile)):
    row = []
    for i in range(len(tile) - 1, -1, -1):
      row.append(tile[i][j])
    new_tile.append(''.join(row))
  return new_tile

def flip(tile):
  return [x[::-1] for x in tile]

def pretty_print(tile):
  for row in tile:
    print(row)

def generate_orientations(tile):
  os = []
  tc = tile
  for i in range(4):
    os.append(tc) 
    tc = rotate(tc)

  for i in range(4):
    os.append(flip(tc))
    tc = rotate(tc)

  return os

def get_border(tile):
  borders = [tile[0], tile[-1]]
  col = [[], []]
  for i in range(len(tile)):
    col[0].append(tile[i][0])
    col[1].append(tile[i][-1])
  return borders + [''.join(col[0]), ''.join(col[1])]

def get_sides(tile, ind1, ind2):
  borders = [tile[ind1]]
  cols = []
  for i in range(len(tile)):
    cols.append(tile[i][ind2])
  return borders + [''.join(cols)]

def first_part(tiles):
  corners = []
  c = []
  for k_m, v_m in tiles.items():
    for vm in generate_orientations(v_m):
      f = True
      for k, v in tiles.items():
        if k == k_m:
          continue
        for a in get_sides(vm, 0, 0):
          for b in get_border(v):
            if a == b or a == b[::-1]:
              f = False
              break
          if not f:
            break
        if not f:
          break
      if f:
        corners.append(k_m)
        c.append(vm)
        break
  return [math.prod(corners), (corners[0], c[0])]

def assemble_two(tile_ind, arr, cur_ind, tiles):
  for k_m, v_m in tiles.items():
    if k_m == tile_ind: continue
    sides = get_sides(arr[cur_ind[0]][cur_ind[1]][tile_ind], -1, -1)
    found = False
    for i in range(len(sides)):
      for ori in generate_orientations(v_m):
        sides2 = get_sides(ori, 0, 0)
        for j in range(len(sides2)):
          if sides[i] == sides2[j] and i == j:
            if i == 0:
              arr[cur_ind[0] + 1][cur_ind[1]] = {k_m: ori}
            else:
              arr[cur_ind[0]][cur_ind[1] + 1] = {k_m: ori}
            found = True
            break
        if found:
          break
      if found:
        break
  return arr

def remove_borders(arr):
  res = []
  for row in arr:
    r = []
    for d in row:
      tile = d[list(d.keys())[0]]
      new_tile = [x[1:-1] for x in tile]
      del new_tile[0]
      del new_tile[-1]
      r.append(new_tile)
    res.append(r)

  f = []
  for i in range(len(res)):
    for k in range(len(res[0][0])):
      row = ''
      for j in range(len(res)):
        row += res[i][j][k]
      f.append(row)
  return f

def sea_monster_pos():
  pos = []
  sm = [line.rstrip() for line in open('sea_monster.txt').readlines()]
  for i in range(len(sm)):
    for j in range(len(sm[i])):
      if sm[i][j] == '#':
        pos.append((i, j))
  return pos

def second_part(tiles, obj):
  N = int(len(tiles.keys()) ** 0.5)
  tile_ind = obj[0]
  arr = []
  for i in range(N):
    row = []
    for j in range(N):
      row.append(None)
    arr.append(row)
  arr[0][0] = {tile_ind: obj[1]}
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      arr = assemble_two(list(arr[i][j].keys())[0], arr, (i, j), tiles)

  sm_pos = sea_monster_pos()
  max_x = max([x for (x, y) in sm_pos])
  max_y = max([y for (x, y) in sm_pos])
  final_img = remove_borders(arr)
  size = len(final_img)
  sm_img = None
  for ori in generate_orientations(final_img):
    has_sm = False
    for i in range(size - max_x):
      for j in range(size - max_y):
        new_sm_pos = [(x + i, y + j) for (x, y) in sm_pos]
        found = True
        for pos in new_sm_pos:
          if not ori[pos[0]][pos[1]] in ['#', 'O']:
            found = False
            break
        if found:
          has_sm = True
          for pos in new_sm_pos:
            l = list(ori[pos[0]])
            l[pos[1]] = 'O'
            ori[pos[0]] = ''.join(l)       
    if has_sm:
      sm_img = ori
      break
  
  return sum([1 for i in range(len(sm_img)) for j in range(len(sm_img[i])) if sm_img[i][j] == '#'])

prod, obj = first_part(d)
print('First part:', prod)
print('Second part:', second_part(d, obj))
