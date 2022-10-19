passports = []
tmp = []
f = open('inp4.txt').readlines()
for i in range(len(f)):
  line = f[i].lstrip().rstrip()
  if len(line) == 0 or i == len(f) - 1:
    if i == len(f) - 1:
      tmp.extend(line.split(' '))
    passports.append(tmp)
    tmp = []
  else:
    tmp.extend(line.split(' '))

fds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
cnt = 0
for passport in passports:
  c = 0
  for pair in passport:
    field = pair.split(':')[0] 
    if field in fds:
      c += 1
  if c == 7:
    cnt += 1

print('First part:', cnt)

def valid_hcl(v):
  if v[0] != '#' or len(v) != 7:
    return False
  try:
    t = int('0x' + v[1:], base=16)
    return True
  except ValueError:
    return False

cnt = 0
for passport in passports:
  flag = True
  c = 0
  for pair in passport:   
    field = pair.split(':')[0] 
    v = pair.split(':')[1]
    if field in fds:
      c += 1
    if field == 'byr':
      if int(v) < 1920 or int(v) > 2002:
        flag = False       
        break
    elif field == 'iyr':
      if int(v) < 2010 or int(v) > 2020:
        flag = False
        break
    elif field == 'eyr':
      if int(v) < 2020 or int(v) > 2030:
        flag = False
        break
    elif field == 'hgt':
      postfix = v[len(v) - 2:]
      if postfix not in ['cm', 'in']:
        flag = False
        break
      av = int(v[:len(v) - 2])
      if (postfix == 'cm' and (av < 150 or av > 193)) or (postfix == 'in' and (av < 59 or av > 76)):
        flag = False
        break
    elif field == 'hcl':
      if not valid_hcl(v):
        flag = False
        break       
    elif field == 'ecl':
      if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        flag = False
        break
    elif field == 'pid':
      for d in v:
        if not d.isdigit():
          flag = False
          break
      if len(v) != 9:
        flag = False
        break
  if flag and c == 7:
    cnt += 1

print('Second part', cnt)
        
        
        
  
