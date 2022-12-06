line = open('6.txt').readline().rstrip()

def solve(line, n):
  i = n
  while len(set(line[i - n:i])) != n:
    i += 1
  return i

print('First part:', solve(line, 4))
print('Second part:', solve(line, 14))
