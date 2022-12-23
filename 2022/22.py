import pdb

maps = {}
toggle = 1
instr = None
cur_pos = None
for i, line in enumerate(open('22.txt').readlines()):
  line = line.rstrip()
  if len(line) == 0:
    toggle = 0
  if toggle:
    j = 0
    while j < len(line):
      if line[j] != ' ':
        if len(maps) == 0:
          cur_pos = [i, j]
        maps[(i, j)] = line[j]
      j += 1
  else:
    instr = line

commands = []
prev_ind = 0
for i, c in enumerate(instr):
  if i == len(instr) - 1:
    commands.append(int(instr[prev_ind:]))
  elif not c.isdigit() :
    commands.extend([int(instr[prev_ind:i]), c])
    prev_ind = i + 1

alt_pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def first_part(commands, maps, cur_pos, alt_pos, cur_facing):
  for i in range(len(commands)):
    if type(commands[i]) == int:
      k = 0
      while k < commands[i]:
        #print(cur_pos)
        #pdb.set_trace()
        cur_pos_save = cur_pos[::1]
        cur_pos[0] += cur_facing[0]
        cur_pos[1] += cur_facing[1]
        if tuple(cur_pos) in maps and maps[tuple(cur_pos)] == '#':
          cur_pos = cur_pos_save
          break
        elif not tuple(cur_pos) in maps:
          if cur_facing[0] == 1:        
            cur_pos = [min([i for i, j in maps.keys() if j == cur_pos[1]]), cur_pos[1]]
          elif cur_facing[0] == -1:
            cur_pos = [max([i for i, j in maps.keys() if j == cur_pos[1]]), cur_pos[1]]
          elif cur_facing[1] == 1:
            cur_pos = [cur_pos[0], min([j for i, j in maps.keys() if i == cur_pos[0]])]
          elif cur_facing[1] == -1:
            cur_pos = [cur_pos[0], max([j for i, j in maps.keys() if i == cur_pos[0]])]
          if maps[tuple(cur_pos)] == '#':
            cur_pos = cur_pos_save
            break
        k += 1
    else:
      if commands[i] == 'R':
        #print('turned right')
        cur_facing = alt_pos[(alt_pos.index(cur_facing) + 1) % len(alt_pos)]
      else:
        #print('turned left')
        cur_facing = alt_pos[alt_pos.index(cur_facing) - 1]
  return 1000 * (cur_pos[0] + 1) + 4 * (cur_pos[1] + 1) + alt_pos.index(cur_facing)

print('First part:', first_part(commands, maps, cur_pos, alt_pos, alt_pos[0]))
