inp = [x.strip() for x in open('10.txt').readlines()]
instr = []
for ins in inp:
  if ins == 'noop':
    instr.append([ins])
  else:
    op, n = ins.split(' ')
    instr.append([op, int(n)])
    instr.append(['noop'])

def first_part(instr):
  X = 1
  summa = 0
  for i, ins in enumerate(instr):
    if (i + 1) % 40 == 20:
      summa += (i + 1) * X
    if ins[0] == 'noop' and instr[i - 1][0] != 'noop':
      X += instr[i - 1][1]
  return summa

def second_part(instr):
  sprite_pos = 1
  ctr_pos = 0
  screen = [list('.' * 40) for i in range(6)]
  for i, ins in enumerate(instr):
    if abs(sprite_pos - (ctr_pos % 40)) <= 1:
      screen[ctr_pos // 40][ctr_pos % 40] = '#'
    if ins[0] == 'noop' and instr[i - 1][0] != 'noop':
      sprite_pos += instr[i - 1][1]
    ctr_pos += 1
  return screen

def pretty_print(screen):
  for row in screen:
    print(''.join(row))

print('First part:', first_part(instr))
print('Second part:')
pretty_print(second_part(instr))
