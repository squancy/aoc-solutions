def parse_input():
  graph = dict()
  cities_to_visit = []
  for line in open('inp9.txt').readlines():
    c1, p1 = line.split(' to ')
    c2, v = p1.split(' = ')
    v = int(v)
    if c1 in graph:
      graph[c1][c2] = v
    else:
      graph[c1] = {c2: v}
    if c2 in graph:
      graph[c2][c1] = v
    else:
      graph[c2] = {c1: v}
    if not c1 in cities_to_visit:
      cities_to_visit.append(c1)
    if not c2 in cities_to_visit:
      cities_to_visit.append(c2)
  return graph, cities_to_visit

def rec(num_of_cities, cities_visited, cur_cost, costs, graph):
  if len(cities_visited) == num_of_cities:
    costs.append(cur_cost)
  else:
    for c in set(graph[cities_visited[-1]].keys()) - set(cities_visited):
      rec(num_of_cities, cities_visited + [c], cur_cost + graph[cities_visited[-1]][c], costs, graph)

def all_path_costs():
  graph, cities_to_visit = parse_input()
  tot_costs = []
  num_of_cities = len(cities_to_visit)
  for c in cities_to_visit:
    costs = []
    rec(len(cities_to_visit), [c], 0, costs, graph)
    tot_costs.extend(costs)
  return tot_costs
print('First part:', min(all_path_costs()))
print('Second part:', max(all_path_costs()))
