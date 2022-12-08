lines = [[int(x) for x in y.strip()] for y in open('8.txt').readlines()]

def is_visible(lines, i, j):
  e = lines[i][j]
  ml = max([x for x in list(lines[i][:j])] + [-1])
  mr = max([x for x in list(lines[i][j + 1:])] + [-1])
  mt = max([x for x in [lines[k][j] for k in range(i)]] + [-1])
  mb = max([x for x in [lines[k][j] for k in range(i + 1, len(lines))]] + [-1])
  return e > ml or e > mr or e > mt or e > mb

def first_part(lines):
  cnt = 0
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if is_visible(lines, i, j):
        cnt += 1
  return cnt

def scenic_score(lines, i, j):
  l, r, t, b = 0, 0, 0, 0 

  while i - t - 1 >= 0:
    t += 1
    if lines[i - t][j] >= lines[i][j]: break

  while j - l - 1 >= 0:
    l += 1
    if lines[i][j - l] >= lines[i][j]: break

  while j + r + 1 < len(lines[i]):
    r += 1
    if lines[i][j + r] >= lines[i][j]: break

  while i + b + 1 < len(lines):
    b += 1
    if lines[i + b][j] >= lines[i][j]: break

  return l * r * t * b

def second_part(lines):
  max_score = 0
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      score = scenic_score(lines, i, j)
      if score > max_score:
        max_score = score
  return max_score

print('First part:', first_part(lines))
print('Second part:', second_part(lines))
