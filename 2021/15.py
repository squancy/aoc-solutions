import heapq
import sys

arr = [[int(x.lstrip().rstrip()) for x in y if x.rstrip().lstrip()] for y in open('inp15.txt').readlines()]
p1arr = arr

n = len(arr)
ffarr = []
for i in range(len(arr) * 5):
  tmp = []
  for j in range(len(arr[0]) * 5):
    tmp.append(None)
  ffarr.append(tmp)

for i in range(len(arr)):
  for j in range(len(arr[i])):
    for k in range(5):
      for l in range(5):
        if arr[i][j] + k + l <= 9:
          v = arr[i][j] + k + l
        else:
          v = (arr[i][j] + k + l) % 10 + 1
        ffarr[n * k + i][n * l + j] = v

arr = ffarr

nodes = []
for i in range(len(arr)):
  for j in range(len(arr[i])):
    nodes.append((i, j))

distances = {}

for node in nodes:
  d = []
  if node[0] > 0:
    d.append(((node[0] - 1, node[1]), arr[node[0] - 1][node[1]]))
  if node[0] < len(arr[node[1]]) - 1:
    d.append(((node[0] + 1, node[1]), arr[node[0] + 1][node[1]]))
  if node[1] > 0:
    d.append(((node[0], node[1] - 1), arr[node[0]][node[1] - 1]))
  if node[1] < len(arr) - 1:
    d.append(((node[0], node[1] + 1), arr[node[0]][node[1] + 1]))
  distances[node] = d

def find_path(g, s, t):
  q = []
  d = {k: sys.maxsize for k in g.keys()}
  p = {}

  d[s] = 0
  heapq.heappush(q, (0, s))

  while q:
    last_w, curr_v = heapq.heappop(q)
    for n, n_w in g[curr_v]:
      cand_w = last_w + n_w 
      if cand_w < d[n]:
        d[n] = cand_w
        p[n] = curr_v
        heapq.heappush(q, (cand_w, n))
  return d[t]

print('First part:', find_path(distances, (0, 0), (len(p1arr) - 1, len(p1arr[0]) - 1)))
print('Second part:', find_path(distances, (0, 0), (len(arr) - 1, len(arr[0]) - 1)))
