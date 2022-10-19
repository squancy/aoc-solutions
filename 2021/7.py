arr = [int(x) for x in open('inp7.txt').readline().split(',')]
d = dict()
for el in arr:
  if el in d:
    d[el] += 1
  else:
    d[el] = 1

"""
  The point where crabs should be aligned in the first part is the median of the array
  Since the distances between the points are minimized in that case
  However this soulution uses brute force and tries every point between the smallest and largest points
"""

def cost(t):
  smallest = 10**10
  for com in range(max(d.keys()) + 1):
    cur_sum = 0
    for el in d.keys():
      if t == 1:
        cur_sum += abs(com - el) * d[el]
      else:
        cur_sum += abs(com - el) * (abs(com - el) + 1) // 2 * d[el]
      if cur_sum >= smallest:
        break
    if cur_sum < smallest:
      smallest = cur_sum
  return smallest

print('First part:', cost(1))
print('Second part:', cost(2))
