import math

inp = [x.rstrip().replace(' ', '') for x in open('inp18.txt').readlines()]

def calc(expr):
  if not expr: return ''
  s = expr.replace('+', '|+|').replace('*', '|*|').split('|')
  v = int(s[0])
  for i in range(1, len(s) - 1, 2):
    if s[i] == '+':
      v += int(s[i + 1])
    elif s[i] == '*':
      v *= int(s[i + 1])
  return str(v)

def calc_precedence(expr):
  if not expr: return ''
  s = expr.replace('+', '|+|').replace('*', '|*|').split('|')
  while '+' in s:
    i = s.index('+')
    s[i] = int(s[i - 1]) + int(s[i + 1])
    s[i - 1] = s[i + 1] = None
    s = [x for x in s if x]
  return str(math.prod([int(x) for x in s if x != '*']))

def eval_expr(expr, func):
  if not expr:
    return ''
  elif not '(' in expr:
    return expr
  else:
    lpos = expr.index('(') 
    level = 1    
    i = lpos + 1
    while level != 0:
      if expr[i] == '(':
        level += 1
      elif expr[i] == ')':
        level -= 1
      i += 1
    rpos = i
    paren_part = expr[lpos + 1:rpos - 1]
    left_part = ''
    left_op = ''
    if lpos != 0:
      left_part = expr[:lpos - 1]
      left_op = expr[lpos - 1]
    right_part = ''
    right_op = ''
    if rpos != len(expr):
      right_part = expr[rpos + 1:]
      right_op = expr[rpos]
    v1 = eval_expr(left_part, func) 
    v2 = func(paren_part) if not '(' in paren_part else eval_expr(paren_part, func)
    v3 = eval_expr(right_part, func)
    return v1 + left_op + func(v2) + right_op + v3

def first_part(inp):
  summa = 0
  for line in inp:
    summa += int(calc(eval_expr(line, calc)))
  return summa

def second_part(inp):
  summa = 0
  for line in inp:
    summa += int(calc_precedence(eval_expr(line, calc_precedence)))
  return summa

print('First part:', first_part(inp))
print('Second part:', second_part(inp))
