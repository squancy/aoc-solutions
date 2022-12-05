intervals = [[[int(z) for z in x.split('-')] for x in y.rstrip().split(',')] for y in open('4.txt').readlines()]

def first_part(intervals):
  return sum((1 if ((l[0][0] <= l[1][0] and l[0][1] >= l[1][1]) or (l[1][0] <= l[0][0] and l[1][1] >= l[0][1])) else 0) for l in intervals)

def second_part(intervals):
  return sum((1 if not (l[1][1] < l[0][0] or l[0][1] < l[1][0]) else 0) for l in intervals)

print('First part:', first_part(intervals))
print('Second part:', second_part(intervals))
