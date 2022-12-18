import re

graph = {}
p = 'Valve ([A-Z]{2}) has flow rate=(\d+); tunnel(?:s|) lead(?:s|) to valve(?:s|) ((?:(?:[A-Z]{2}), |(?:[A-Z]{2}))+)'
for line in open('16.txt'):
  line = line.strip()
  m = re.match(p, line) 
  graph[m.group(1)] = {
    'rate': int(m.group(2)),
    'nbs': [x.strip() for x in m.group(3).split(',')]
  }

nz_valves = [x for x in graph if graph[x]['rate'] != 0]

def shortest_path(graph, node1, node2):
  path_list = [[node1]]
  path_index = 0
  previous_nodes = {node1}
  if node1 == node2:
    return []
      
  while path_index < len(path_list):
    current_path = path_list[path_index]
    last_node = current_path[-1]
    next_nodes = graph[last_node]['nbs']
    if node2 in next_nodes:
      current_path.append(node2)
      return current_path
    for next_node in next_nodes:
      if not next_node in previous_nodes:
        new_path = current_path[:]
        new_path.append(next_node)
        path_list.append(new_path)
        previous_nodes.add(next_node)
    path_index += 1
  return current_path

pairs = {}
nodes = ['AA'] + nz_valves
for i in range(len(nodes)):
  for j in range(len(nodes)):
    if nodes[i] == nodes[j]: continue
    pairs[(nodes[i], nodes[j])] = shortest_path(graph, nodes[i], nodes[j]) 

def calc_cost(nodes, open_nodes, minutes):
  cost = 0
  m = 0
  for i, node in enumerate(nodes):
    if i in open_nodes:
      m += 1
      cost += (minutes - m) * graph[node]['rate']
    m += 1
  return cost

def rec(pairs, cur_node, cur_path, paths, visited_nzs, inds):
  remaining = set(nz_valves) - set(visited_nzs)
  if len(remaining) == 0:
    paths.add((tuple(cur_path), tuple(inds)))
  for nzv in remaining:
    prop_path = pairs[(cur_node, nzv)] if len(cur_path) == 0 else cur_path + pairs[(cur_node, nzv)][1:]
    if len(prop_path) + len(inds) > 30:
      paths.add((tuple(cur_path), tuple(inds)))
    else:
      rec(pairs, nzv, prop_path, paths, visited_nzs + [nzv], inds + [len(prop_path) - 1])
  return 0

def first_part(pairs):
  paths = set()
  rec(pairs, 'AA', [], paths, [], [])
  max_pressure = 0
  for path in paths:
    p = calc_cost(path[0], path[1], 30)
    if p > max_pressure:
      max_pressure = p
  return max_pressure

def rec_e(pairs, cur_node, cur_node_e, cur_path, cur_path_e, paths, visited_nzs, visited_nzs_e, inds, inds_e):
  remaining = set(nz_valves) - set(visited_nzs) - set(visited_nzs_e)
  for nzv in remaining:
    if len(cur_path_e) == 0:
      prop_path_e = pairs[(cur_node_e, nzv)]
    else:
      prop_path_e = cur_path_e + pairs[(cur_node_e, nzv)][1:]
    prop_path = pairs[(cur_node, nzv)] if len(cur_path) == 0 else cur_path + pairs[(cur_node, nzv)][1:]
    
    # only assumed on this specific input
    # without this optimization the code is still correct but takes much more time to run
    if ((len(cur_path) + len(inds) >= 16 and len(set(visited_nzs) & set(nz_valves)) < 5)
      or (len(cur_path_e) + len(inds_e) >= 16 and len(set(visited_nzs_e) & set(nz_valves)) < 5)):
      break

    if len(prop_path_e) + len(inds_e) + 1 <= 26 and len(cur_path_e) + len(inds_e) <= len(cur_path) + len(inds):
      rec_e(pairs, cur_node, nzv, cur_path, prop_path_e, paths, visited_nzs, visited_nzs_e + [nzv], inds, inds_e + [len(prop_path_e) - 1])
    elif len(prop_path) + len(inds) + 1 <= 26 and len(cur_path_e) + len(inds_e) > len(cur_path) + len(inds):
      rec_e(pairs, nzv, cur_node_e, prop_path, cur_path_e, paths, visited_nzs + [nzv], visited_nzs_e, inds + [len(prop_path) - 1], inds_e)
    else:
      paths.add((tuple(cur_path), tuple(inds), tuple(cur_path_e), tuple(inds_e)))
  paths.add((tuple(cur_path), tuple(inds), tuple(cur_path_e), tuple(inds_e)))

def second_part(pairs):
  paths = set()
  rec_e(pairs, 'AA', 'AA', [], [], paths, [], [], [], [])
  max_p = 0
  for path in paths:
    p = calc_cost(path[0], path[1], 26) + calc_cost(path[2], path[3], 26)
    if p > max_p:
      max_p = p
  return max_p

print('First part:', first_part(pairs))
print('Second part:', second_part(pairs))
