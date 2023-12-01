def find_num(s):
  i = 0
  while i < len(s):
    if s[i].isdigit():
      return s[i], i
    i += 1
 
def first_part(lines):
  total = 0
  for line in lines:
    total += int(find_num(line)[0] + find_num(line[::-1])[0]) 
  return total

def second_part(lines):
  total = 0
  D = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
    'eight': 8, 'nine': 9
  }

  for line in lines:
    s1 = find_num(line)
    e1 = find_num(line[::-1])

    s = {len(line): 0}
    e = {len(line): 0}

    for k, v in D.items():
      if k in line:
        s[line.index(k)] = str(v)
      if k[::-1] in line[::-1]:
        e[line[::-1].index(k[::-1])] = str(v)

    s = s[min(s.keys())], min(s.keys())
    e = e[min(e.keys())], min(e.keys())

    fs = s[0]
    if s1[1] < s[1]:
      fs = s1[0]
    fe = e[0]

    if e1[1] < e[1]:
      fe = e1[0]

    total += int(fs + fe) 
  return total

lines = open('1.txt').readlines()
print('First part:', first_part(lines))
print('Second part:', second_part(lines))
