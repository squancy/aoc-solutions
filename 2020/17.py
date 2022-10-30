inp = [None, None, None]
inp[1] = [x.rstrip() for x in open('inp17.txt').readlines()]
inp[0] = inp[2] = ['.' * len(inp[1][0]) for i in range(len(inp[1][0]))]

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

def first_part(inp):
  for i in range(1):
    nx = [[y for y in x] for x in inp]
    for x in range(len(inp)):
      for y in range(len(inp[x])):
        for z in range(len(inp[x][y])):
          r = '#' if check_state(inp[x][y][z], (x, y, z), inp) else '.'
          nx[x][y] = nx[x][y][:z] + r + nx[x][y][z + 1:]
    l = len(inp)
    print(nx)
    print(inp)
    inp = nx
    inp = [['.' + y + '.' for y in x] for x in inp] 
    inp = [['.' * (l + 2)] + x + ['.' * (l + 2)] for x in inp]
    inp.insert(0, ['.' * (l + 2) for i in range(l + 2)])
    inp.append(['.' * (l + 2) for i in range(l + 2)])
  return inp

inp = first_part(inp)
cnt = 0
for x in inp:
  for y in x:
    cnt += y.count('#')
print(cnt)
