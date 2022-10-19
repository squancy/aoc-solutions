arr = [[int(k) for k in list(x.lstrip().rstrip())] for x in open('inp9.txt').readlines()]
hm = 0
low_points = []
for i in range(len(arr)):
  for j in range(len(arr[i])):
    if ((j > 0 and arr[i][j - 1] <= arr[i][j]) or 
        (j < len(arr[i]) - 1 and arr[i][j + 1] <= arr[i][j]) or
        (i > 0 and arr[i - 1][j] <= arr[i][j]) or
        (i < len(arr) - 1 and arr[i + 1][j] <= arr[i][j])):
      continue
    hm += arr[i][j] + 1
    low_points.append((i, j))
print('First part:', hm)

def basin_size(i, j, mp):
  if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[i]) or arr[i][j] == 9:
    return
  if (i, j) not in mp:
    mp.append((i, j))
  else:
    return
  basin_size(i, j - 1, mp)
  basin_size(i, j + 1, mp)
  basin_size(i - 1, j, mp)
  basin_size(i + 1, j, mp)

basin_sizes = []
for p in low_points:
  mp = []
  basin_size(p[0], p[1], mp)
  basin_sizes.append(len(mp))
basin_sizes = sorted(basin_sizes)
print('Second part:', basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
