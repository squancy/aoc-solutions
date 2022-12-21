import re, sympy

d = {}
p = '\+|\-|\*|\/' 
pe = '[0-9\(\)\+\-\/\*]+'
x = sympy.symbols('x')
for line in open('21.txt').readlines():
  line = line.strip()
  k, v = line.split(':')
  v = v.strip()
  if v.isnumeric():
    d[k] = int(v)
  else:
    if '+' in v:
      op = '+'
    elif '-' in v:
      op = '-'
    elif '*' in v:
      op = '*'
    else:
      op = '//'
    op1, op2 = re.split(p, v)
    d[k] = [op1.strip(), op, op2.strip()]

def compute(d, di):
  if type(d) == int:
    return d
  if d[1] == '+':
    return compute(di[d[0]], di) + compute(di[d[2]], di)
  elif d[1] == '-':
    return compute(di[d[0]], di) - compute(di[d[2]], di)
  elif d[1] == '*':
    return compute(di[d[0]], di) * compute(di[d[2]], di)
  else:
    return compute(di[d[0]], di) // compute(di[d[2]], di)

def equation(d, di):
  if type(d) == int:
    return d
  left_expr = x if d[0] == 'humn' else equation(di[d[0]], di)
  right_expr = x if d[2] == 'humn' else equation(di[d[2]], di)
  ints = type(left_expr) == int and type(right_expr) == int
  if d[1] == '+':
    return int(left_expr + right_expr) if ints else (left_expr + right_expr)
  elif d[1] == '-':
    return int(left_expr - right_expr) if ints else (left_expr - right_expr)
  elif d[1] == '*':
    return int(left_expr * right_expr) if ints else (left_expr * right_expr)
  elif d[1] == '//':
    return int(left_expr // right_expr) if ints else (left_expr / right_expr)

print('First part:', compute(d['root'], d))
left = equation(d[d['root'][0]], d)
right = equation(d[d['root'][2]], d)
print('Second part:', sympy.solve(left - right, x)[0])
