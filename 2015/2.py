inp = [[int(x) for x in y.rstrip().split('x')] for y in open('inp2.txt').readlines()]

def first_part(lines):
  summa = 0
  for l in lines:
    summa += 2 * (l[0] * l[1] + l[0] * l[2] + l[1] * l[2]) + min(l[0] * l[1], l[0] * l[2], l[1] * l[2])
  return summa

def second_part(lines):
  summa = 0
  for l in lines:
    l = sorted(l) 
    summa += 2 * (l[0] + l[1]) + l[0] * l[1] * l[2]
  return summa

print('First part:', first_part(inp))
print('Second part:', second_part(inp))
