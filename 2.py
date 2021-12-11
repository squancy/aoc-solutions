inp = [l.lstrip().rstrip() for l in open('inp2.txt').readlines()]
pos1 = [0, 0]
pos2 = [0, 0]
aim = 0
for instruction in inp:
  command = instruction.split(' ')[0]
  arg = instruction.split(' ')[1]
  if command == 'forward':
    pos1[0] += int(arg)
    pos2[0] += int(arg)
    pos2[1] += int(arg) * aim
  elif command == 'down':
    pos1[1] += int(arg)
    aim += int(arg)
  else:
    pos1[1] -= int(arg)
    aim -= int(arg)
print('First part:', pos1[0] * pos1[1])
print('Second part:', pos2[0] * pos2[1])
