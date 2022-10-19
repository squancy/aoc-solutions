arr = [[int(y) for y in list(x.lstrip().rstrip())] for x in open('inp11.txt').readlines()]
arr2 = [[int(y) for y in list(x.lstrip().rstrip())] for x in open('inp11.txt').readlines()]

def should_continue(arr, tracked):
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] > 9 and (i, j) not in tracked:
        return True
  return False

def is_zero(arr):
  for row in arr:
    for el in row:
      if el != 0:
        return False
  return True

flashes = 0
steps = 0

def simulate(arr, t):
  t[0] += 1
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      arr[i][j] += 1
  
  tracked = []
  while should_continue(arr, tracked):
    for i in range(len(arr)):
      for j in range(len(arr[i])):
        if arr[i][j] > 9 and (i, j) not in tracked:
          t[1] += 1
          tracked.append((i, j))
          
          if i > 0 and j > 0:
            arr[i - 1][j - 1] += 1
          if i > 0:
            arr[i - 1][j] += 1
          if i > 0 and j < len(arr[i]) - 1:
            arr[i - 1][j + 1] += 1
          if j > 0:
            arr[i][j - 1] += 1
          if j < len(arr[i]) - 1:
            arr[i][j + 1] += 1
          if i < len(arr) - 1 and j > 0:
            arr[i + 1][j - 1] += 1
          if i < len(arr) - 1:
            arr[i + 1][j] += 1
          if i < len(arr) - 1 and j < len(arr[i]) - 1:
            arr[i + 1][j + 1] += 1
  for p in tracked:
    arr[p[0]][p[1]] = 0

p1 = [0, 0]
p2 = [0, 0]
for i in range(100):
  simulate(arr, p1)

while not is_zero(arr2):
  simulate(arr2, p2)

print('First part:', p1[1])
print('Second part:', p2[0])
