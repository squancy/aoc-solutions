intervals = [[[int(z) for z in x.split('-')] for x in y.rstrip().split(',')] for y in open('4.txt').readlines()]

def first_part(intervals):
  cnt = 0
  for line in intervals:
    if (line[0][0] <= line[1][0] and line[0][1] >= line[1][1]) or (line[1][0] <= line[0][0] and line[1][1] >= line[0][1]):
      cnt += 1
  return cnt

def second_part(intervals):
  cnt = 0
  for line in intervals:
    if not (line[1][1] < line[0][0] or line[0][1] < line[1][0]):
      cnt += 1
  return cnt

print('First part:', first_part(intervals))
print('Second part:', second_part(intervals))
