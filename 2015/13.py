import re

p = re.compile('([A-Za-z]+) would (gain|lose) ([0-9]+) happiness units by sitting next to ([A-Za-z]+)\.')

def parse_input():
  graph = {}
  for line in open('inp13.txt').readlines():
    line = line.rstrip()
    s = re.search(p, line)
    name1 = s.group(1)
    units = int(s.group(3)) * (1 if 'gain' in line else -1)
    name2 = s.group(4)
    if name1 in graph:
      graph[name1][name2] = units
    else:
      graph[name1] = {name2: units}
  return graph

graph = parse_input()

def rec(num_of_points, cur_names, cnames_arr, names):
  if len(cur_names) == num_of_points:
    cnames_arr.append(cur_names)
  else:
    for name in names:
      if not name in cur_names:
        rec(num_of_points, cur_names + [name], cnames_arr, names)

def get_happiness(names):
  h = 0
  for i in range(len(names)):
    left_nb_ind = i - 1
    right_nb_ind = (i + 1) % len(names)
    h += graph[names[i]][names[left_nb_ind]] + graph[names[i]][names[right_nb_ind]]
  return h

def max_h(names):
  hs = []
  for name in names:
    hs.append(get_happiness(name))
  return max(hs)

def run():
  cnames_arr = []
  rec(len(graph.keys()), [], cnames_arr, list(graph.keys()))
  return max_h(cnames_arr)

print('First part:', run())

graph['x'] = {}
for name in graph.keys():
  graph['x'][name] = 0
  graph[name]['x'] = 0

print('Second part:', run())
