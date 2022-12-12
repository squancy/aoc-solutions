from collections import defaultdict

def get_nbs(inp, i, j):
  arr = []
  for c1, c2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
    if c1 < 0 or c2 < 0: continue
    try:
      x = inp[c1][c2]
      arr.append([x, (c1, c2)])
    except:
      pass
  return arr

inp = [[y for y in x.strip()] for x in open('12.txt').readlines()]

S = None
E = None

for i in range(len(inp)):
  for j in range(len(inp[i])):
    if inp[i][j] == 'E':
      inp[i][j] = 'z'
      E = (i, j)
    elif inp[i][j] == 'S':
      inp[i][j] = 'a'
      S = (i, j)

graph = defaultdict(list)

for i in range(len(inp)):
  for j in range(len(inp[i])):
    nbs = get_nbs(inp, i, j) 
    for nb in nbs:
      if ord(nb[0]) - ord(inp[i][j]) <= 1:
        graph[(i, j)].append(nb[1])

def shortest_path(graph, node1, node2):
  path_list = [[node1]]
  path_index = 0
  previous_nodes = {node1}
  if node1 == node2:
    return 0
      
  while path_index < len(path_list):
    current_path = path_list[path_index]
    last_node = current_path[-1]
    next_nodes = graph[last_node]
    if node2 in next_nodes:
      current_path.append(node2)
      return len(current_path) - 1
    for next_node in next_nodes:
      if not next_node in previous_nodes:
        new_path = current_path[:]
        new_path.append(next_node)
        path_list.append(new_path)
        previous_nodes.add(next_node)
    path_index += 1
  return -1

def second_part(graph, E):
  min_cost = None
  for i in range(len(inp)):
    for j in range(len(inp[i])):
      if inp[i][j] != 'a': continue
      mc = shortest_path(graph, (i, j), E)
      if mc == -1: continue
      if min_cost == None or mc < min_cost:
        min_cost = mc
  return min_cost

print('First part:', shortest_path(graph, S, E))
print('Second part:', second_part(graph, E))
