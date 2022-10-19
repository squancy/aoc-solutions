import itertools

"""
  The 2nd part is pretty slow, takes a few seconds to run
"""

lines = [x.lstrip().rstrip() for x in open('inp12.txt').readlines()]
graph = dict()
for line in lines:
  fr, to = line.split('-')
  if fr in graph:
    graph[fr].append(to)
  elif fr not in graph:
    graph[fr] = [to]

  if to in graph:
    graph[to].append(fr)
  else:
    graph[to] = [fr]

def find_path(path, tracked, cur_node, special_small_cave, all_paths):
  if ((cur_node in tracked and cur_node != special_small_cave) or
    (cur_node in tracked and cur_node == special_small_cave and tracked[cur_node] > 1)):
    return
  if cur_node.islower():
    if cur_node not in tracked:
      tracked[cur_node] = 1
    else:
      tracked[cur_node] += 1
  if cur_node == 'end':
    all_paths.append(path)
    return
  path.append(cur_node)
  for node in graph[cur_node]:
    path_copy = [x for x in path]
    tracked_copy = {x: tracked[x] for x in tracked}
    find_path(path_copy, tracked_copy, node, special_small_cave, all_paths)

all_paths = []
find_path([], dict(), 'start', None, all_paths)
all_paths.sort()

print('First part:', len(list(k for k,_ in itertools.groupby(all_paths))))

all_paths = []
for k in graph:
  if k.islower() and k not in ['start', 'end']:
    find_path([], dict(), 'start', k, all_paths)
all_paths.sort()

print('Second part:', len(list(k for k,_ in itertools.groupby(all_paths))))
