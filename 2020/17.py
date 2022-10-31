inp = [None, None, None]
inp[1] = [x.rstrip() for x in open('inp17.txt').readlines()]
inp[0] = inp[2] = ['.' * len(inp[1][0]) for i in range(len(inp[1][0]))]

sl = [x.rstrip() for x in open('inp17.txt').readlines()]
coords = {(x, y, 0, 0): 1 for x in range(len(sl)) for y in range(len(sl[x])) if sl[x][y] == '#'}

def check_state(cur_state, pos, inp):
  active_nb = 0
  for x in range(-1, 2):
    for y in range(-1, 2):
      for z in range(-1, 2):
        if x == y == z == 0:
          continue
        x_pos = pos[0] + x if 0 <= pos[0] + x < len(inp) else None
        y_pos = pos[1] + y if 0 <= pos[1] + y < len(inp) else None
        z_pos = pos[2] + z if 0 <= pos[2] + z < len(inp) else None
        if None in [x_pos, y_pos, z_pos]:
          continue
        if inp[x_pos][y_pos][z_pos] == '#':
          active_nb += 1
  return (2 <= active_nb <= 3 and cur_state == '#') or (active_nb == 3 and cur_state == '.')

def add_padding(inp):
  C = 2
  l = len(inp[0])
  inp = [['.' + y + '.' for y in x] for x in inp] 
  inp = [['.' * (l + C)] + x + ['.' * (l + C)] for x in inp]
  inp.insert(0, ['.' * (l + C) for i in range(l + C)])
  inp.append(['.' * (l + C) for i in range(l + C)])
  return inp

def simulate_3D(inp):
  for i in range(6):
    nx = [[y for y in x] for x in inp]
    for x in range(len(inp)):
      for y in range(len(inp[x])):
        for z in range(len(inp[x][y])):
          r = '#' if check_state(inp[x][y][z], (x, y, z), inp) else '.'
          nx[x][y] = nx[x][y][:z] + r + nx[x][y][z + 1:]
    inp = nx
    inp = add_padding(inp)
  return inp

def first_part(inp):
  for i in range(5):
    inp = add_padding(inp)
  inp = simulate_3D(inp)
  cnt = 0
  for x in inp:
    for y in x:
      cnt += y.count('#')
  return cnt

def check_nb_4D(coords, pos, cur_cube):
  active_nb = 0
  for x in range(-1, 2):
    for y in range(-1, 2):
      for z in range(-1, 2):
        for w in range(-1, 2):
          if x == y == z == w == 0: continue
          if coords.get((pos[0] + x, pos[1] + y, pos[2] + z, pos[3] + w), 0):
            active_nb += 1
  return (2 <= active_nb <= 3 and cur_cube) or (active_nb == 3 and not cur_cube)

def simulate_4D(size, coords):
  bound = 1
  for i in range(6):
    ch = {}
    for x in range(-bound, size + 1):
      for y in range(-bound, size + 1):
        for z in range(-bound, bound + 1):
          for w in range(-bound, bound + 1):
            cur_cube = coords.get((x, y, z, w), 0)
            r = check_nb_4D(coords, (x, y, z, w), cur_cube)
            if (cur_cube and not r) or (not cur_cube and r): 
              ch[(x, y, z, w)] = r
    for k, v in ch.items():
      coords[k] = v
    size += 1
    bound += 1
  return coords

def second_part(coords):
  return len([1 for k, v in simulate_4D(len(sl), coords).items() if v])

print('First part:', first_part(inp))
print('Second part:', second_part(coords))
