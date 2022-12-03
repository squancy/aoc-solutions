lines = [x.rstrip() for x in open('3.txt').readlines()]

def first_part(lines):
  summa = 0
  for line in lines:
    common = ''.join((set(line[:len(line) // 2]) & set(line[len(line) // 2:])))
    summa += ord(common) - 96 if common.islower() else ord(common) - 38
  return summa

def second_part(lines):
  summa = 0
  for i in range(2, len(lines), 3):
    common = ''.join(set(lines[i]) & set(lines[i - 1]) & set(lines[i - 2]))
    summa += ord(common) - 96 if common.islower() else ord(common) - 38
  return summa

print('First part:', first_part(lines))
print('Second part:', second_part(lines))
