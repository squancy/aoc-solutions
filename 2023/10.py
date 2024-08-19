inp = [[x for x in line.strip()] for line in open('10.txt')]

def find_loop(inp):
  S_pos = [(i, j) for i in range(len(inp)) for j in range(len(inp[0])) if inp[i][j] == 'S'][0]
  p = pp = S_pos
  visited_nodes = dict()
  i = 0
  while p != S_pos or i == 0:
    orig_p = p
    i += 1
    visited_nodes[p] = 1
    cur_pipe = inp[p[0]][p[1]]
    if cur_pipe == '|':
      p = (p[0] + 1, p[1]) if pp[0] < p[0] else (p[0] - 1, p[1])
    elif cur_pipe == '-':
      p = (p[0], p[1] + 1) if pp[1] < p[1] else (p[0], p[1] - 1)
    elif cur_pipe == 'L':
      p = (p[0] - 1, p[1]) if pp[0] == p[0] else (p[0], p[1] + 1)
    elif cur_pipe == 'J':
      p = (p[0] - 1, p[1]) if pp[0] == p[0] else (p[0], p[1] - 1)
    elif cur_pipe == '7':
      p = (p[0] + 1, p[1]) if pp[0] == p[0] else (p[0], p[1] - 1)
    elif cur_pipe == 'F':
      p = (p[0] + 1, p[1]) if pp[0] == p[0] else (p[0], p[1] + 1)
    elif cur_pipe == 'S':
      if inp[p[0] - 1][p[1]] in ['|', '7', 'F']:
        p = (p[0] - 1, p[1])
      elif inp[p[0] + 1][p[1]] in ['|', 'L', 'J']:
        p = (p[0] + 1, p[1])
      elif inp[p[0]][p[1] + 1] in ['-', '7', 'J']:
        p = (p[0], p[1] + 1)
      else: 
        p = (p[0], p[1] - 1)
    pp = orig_p
  return len(visited_nodes) // 2, visited_nodes

def num_of_intersections(i, j, inp):
  cnt = 0
  while j < len(inp[i]) - 1:
    c = inp[i][j - 1] + inp[i][j] + inp[i][j + 1]
    if c in ['.|.', '|||', '||L', '||F', 'J||', '7||']:
      cnt += 1
    j += 1
  return cnt

def clean_inp(inp, loop):
  for i in range(len(inp)):
    for j in range(len(inp[i])):
      if not (i, j) in loop:
        inp[i][j] = '.'

def second_part(inp, loop):
  clean_inp(inp, loop)
  for row in inp:
    print(''.join(row))
  cnt = 0 
  for i in range(len(inp)):
    for j in range(len(inp[i])):
      if inp[i][j] in ['|', '-', 'L', 'J', '7', 'F', 'S']:
        continue
      n = num_of_intersections(i, j, inp)
      if n % 2 == 1:
        cnt += 1
  return cnt

fp, loop = find_loop(inp)
print('First part:', fp)
print('Second part:', second_part(inp, loop))
