inp = open('inp3.txt').readline().rstrip()

def first_part(inp):
  visited_houses = [[0, 0]]
  cur_pos = [0, 0]
  for d in inp:
    if d == '>':
      cur_pos[0] += 1
    elif d == '<':
      cur_pos[0] -= 1
    elif d == '^':
      cur_pos[1] += 1
    else:
      cur_pos[1] -= 1
    if not cur_pos in visited_houses:
      visited_houses.append(cur_pos[:])
  return len(visited_houses)

def second_part(inp):
  visited_houses = [[0, 0]]
  santa_pos = [0, 0]
  rsanta_pos = [0, 0]
  t = 0
  for d in inp:
    pos = santa_pos if not t else rsanta_pos
    if d == '>':
      pos[0] += 1
    elif d == '<':
      pos[0] -= 1
    elif d == '^':
      pos[1] += 1
    else:
      pos[1] -= 1
    if not pos in visited_houses:
      visited_houses.append(pos[:])
    t = not t
  return len(visited_houses)

print('First part:', first_part(inp))
print('Second part:', second_part(inp))
