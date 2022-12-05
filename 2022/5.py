crates = [[] for _ in range(9)]
instr = []
toggle = 1

for line in open('5.txt').readlines():
  line = line.rstrip()
  if not line:
    toggle = not toggle
  elif toggle and '[' in line:
    o = line.replace('    ', ' ').split(' ')
    for i in range(len(o)):
      if o[i]:
        crates[i].append(o[i].replace('[', '').replace(']', ''))
  elif not toggle:
    sp = line.split(' ')
    instr.append([int(sp[1]), int(sp[3]), int(sp[5])])

def solve(instr, crates, step):
  crates = [[y for y in x] for x in crates]
  for ins in instr:
    crates[ins[2] - 1][:0] = crates[ins[1] - 1][:ins[0]][::step]
    del crates[ins[1] - 1][:ins[0]]

  return ''.join(x[0] for x in crates if x)

print('First part:', solve(instr, crates, -1))
print('Second part:', solve(instr, crates, 1))
