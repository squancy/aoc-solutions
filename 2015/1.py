inp = open('inp1.txt').readline().rstrip()

def first_part(inp):
  return inp.count('(') - inp.count(')')

def second_part(inp):
  i = 0
  val = 0
  while val != -1:
    val += 1 if inp[i] == '(' else -1
    i += 1
  return i

print('First part:', first_part(inp))
print('Second part:', second_part(inp))
