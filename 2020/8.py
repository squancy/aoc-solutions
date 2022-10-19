instr = [[y.rstrip() for y in x.split(' ')] for x in open('inp.txt').readlines()]

def run_program(instr):
  acc = 0
  already_executed = []
  i = 0
  loop = False
  while i < len(instr):
    if i in already_executed:
      loop = True
      break
    jumped = False
    ins = instr[i]
    already_executed.append(i)
    if instr[i][0] == 'acc':
      acc += int(instr[i][1])
    elif instr[i][0] == 'jmp':
      i += int(instr[i][1])
      jumped = True
    
    if not jumped:
      i += 1

  return [loop, acc]

print('First part:', run_program(instr)[1])  

all_perms = []
for i in range(len(instr)):
  if instr[i][0] == 'nop':
    instr[i][0] = 'jmp'
    all_perms.append([[y for y in x] for x in instr])
    instr[i][0] = 'nop'
  elif instr[i][0] == 'jmp':
    instr[i][0] = 'nop'
    all_perms.append([[y for y in x] for x in instr])
    instr[i][0] = 'jmp'

for p in all_perms:
  v = run_program(p)
  if not v[0]:
    print('Second part:', v[1])
    break
