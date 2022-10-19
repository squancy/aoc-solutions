lines = [x.lstrip().rstrip() for x in open('inp10.txt').readlines()]
openings = ['(', '{', '[', '<']
closings = [')', '}', ']', '>']
lookup = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores = {')': 1, ']': 2, '}': 3, '>': 4}
summa = 0
p2s = []
for line in lines:
  search = []
  flag = False
  p2 = 0
  for c in line:
    if c in closings and c != search[-1]:
      summa += lookup[c]
      flag = True
      break
    if c in openings:
      search.append(closings[openings.index(c)])
    else:
      del search[-1]
  if not flag:
    s = ''.join(search[::-1])
    for ch in s:
      p2 = p2 * 5 + scores[ch]
    p2s.append(p2)
print('First part:', summa)
print('Second part:', sorted(p2s)[len(p2s) // 2])
