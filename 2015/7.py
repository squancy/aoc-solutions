all_instr = {line.split(' -> ')[1].rstrip(): line.split(' -> ')[0] for line in open('inp7.txt').readlines()}

def calc_res(instr, known_vals):
  if instr.isnumeric():
    return int(instr)
  elif 'AND' in instr:
    v1, v2 = instr.split(' AND ')
    return known_vals[v1] & known_vals[v2]
  elif 'OR' in instr:
    v1, v2 = instr.split(' OR ')
    return known_vals[v1] | known_vals[v2]
  elif 'LSHIFT' in instr:
    v, s = instr.split(' LSHIFT ')
    s = int(s)
    return known_vals[v] << s
  elif 'RSHIFT' in instr:
    v, s = instr.split(' RSHIFT ')
    s = int(s)
    return known_vals[v] >> s
  elif 'NOT' in instr:
    v = instr.replace('NOT ', '')
    return 2 ** 16 - 1 - known_vals[v]
  else:
    return known_vals[instr]

def extract_vars(instr):
  binary_operators = ['AND', 'OR', 'LSHIFT', 'RSHIFT']
  for bo in binary_operators:
    if bo in instr:
      return instr.split(f' {bo} ')
  if 'NOT' in instr:
    return [instr.replace('NOT ', '')]
  if not instr.isnumeric():
    return [instr]
  return []

def eval_instr(output, instr, known_vals, all_instr):
  operands = extract_vars(instr)
  not_known = []
  for op in operands:
    if not op in known_vals and not op.isnumeric():
      not_known.append(op)
    elif op.isnumeric():
      known_vals[op] = int(op)
  if len(not_known) == 0:
    known_vals[output] = calc_res(instr, known_vals)
  else:
    for op in not_known + [output]:
      eval_instr(op, all_instr[op], known_vals, all_instr)

known_vals = {}
eval_instr('a', all_instr['a'], known_vals, all_instr)
print('First part:', known_vals['a'])
all_instr['b'] = str(known_vals['a'])
known_vals = {}
eval_instr('a', all_instr['a'], known_vals, all_instr)
print('Second part:', known_vals['a'])
