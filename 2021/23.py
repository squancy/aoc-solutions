from collections import namedtuple                                                            
import heapq as hq                                                                           
import itertools as itt                                                                      

"""
  First part is solved by a slowish recursive approach, it takes a few minutes to run
  Second part uses a version of Dijkstra where new nodes are generated from the current state
"""

pairs = (
  ('A', 'A', 'A', 'A'),
  ('B', 'B', 'B', 'B'),
  ('C', 'C', 'C', 'C'),
  ('D', 'D', 'D', 'D')
)

room_lookup = {
  'A': 0,
  'B': 1,
  'C': 2,
  'D': 3
}

cost_lookup = {
  'A': 1,
  'B': 10,
  'C': 100,
  'D': 1000
}

pos_lookup = {
  'A': 2,
  'B': 4,
  'C': 6,
  'D': 8
}

room_lookup = {
  2: 0,
  4: 1,
  6: 2,
  8: 3
}

rpos_lookup = {
  0: 2,
  1: 4,
  2: 6,
  3: 8
}

ordered_rooms = [['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]
step_out = [1, 3, 5, 7, 9]
out_indexes = [2, 4, 6, 8]

least_cost = 10**10

def play(hallway, room1, room2, room3, room4, cost):
  global least_cost

  if cost >= least_cost:
    return cost

  if room1 == ['A', 'A'] and room2 == ['B', 'B'] and room3 == ['C', 'C'] and room4 == ['D', 'D']:
    if cost < least_cost:
      least_cost = cost
    return cost 
  else:
    # moves out of a room into the hallway
    rooms = [room1, room2, room3, room4]
    calls = []
    for i in range(len(rooms)):
      cur_room = [x for x in rooms[i]]
      possible_indexes = []
      if hallway[step_out[i]] == 0:
        possible_indexes.append(step_out[i]) 
        k = step_out[i] - 1
        while k >= 0 and hallway[k] == 0:
          if k not in out_indexes:
            possible_indexes.append(k)
          k -= 1
      if hallway[step_out[i + 1]] == 0:
        possible_indexes.append(step_out[i + 1]) 
        k = step_out[i + 1] + 1
        while k < len(hallway) and hallway[k] == 0:
          if k not in out_indexes:
            possible_indexes.append(k)
          k += 1
      for pi in possible_indexes:
        if rooms[i][0] != 0 and rooms[i] != ordered_rooms[i] and hallway[rpos_lookup[i]] == 0:
          cur_room[0] = 0
          hc = [x for x in hallway]
          hc[pi] = rooms[i][0]
          rms = [[x for x in cur_room] if j == i else [y for y in rooms[j]] for j in range(4)]
          calls.append(play(hc, *rms, cost + (1 + abs(pi - rpos_lookup[i])) * cost_lookup[hc[pi]]))
        elif rooms[i][0] == 0 and rooms[i][1] != 0 and rooms[i][1] != ordered_rooms[i][1] and hallway[rpos_lookup[i]] == 0:
          cur_room[1] = 0
          hc = [x for x in hallway]
          hc[pi] = rooms[i][1]
          rms = [[x for x in cur_room] if j == i else [y for y in rooms[j]] for j in range(4)]
          calls.append(play(hc, *rms, cost + (2 + abs(pi - rpos_lookup[i])) * cost_lookup[hc[pi]]))       
    
    # moves from the hallway into a side room
    for i in range(len(hallway)):
      if hallway[i] != 0:
        pos_to_go = pos_lookup[hallway[i]]
        room_ind = room_lookup[pos_to_go]
        room_to_go = [x for x in rooms[room_ind]]
        both_empty = room_to_go[0] == 0 and room_to_go[1] == 0
        upper_empty = room_to_go[0] == 0 and room_to_go[1] == hallway[i]
        if both_empty or upper_empty:
          hc = [x for x in hallway]
          rms = [room_to_go if i == room_ind else rooms[i] for i in range(4)]
          m = 2 if both_empty else 1
          ind = 1 if both_empty else 0
          if pos_to_go == i:
            hc[i] = 0
            room_to_go[ind] = hallway[i]
            calls.append(play(hc, *rms, cost + m * cost_lookup[hallway[i]]))
          elif i < pos_to_go:
            flag = True
            for k in range(i + 1, pos_to_go + 1):
              if hallway[k] != 0:
                flag = False
                break
            if flag:
              hc[i] = 0
              room_to_go[ind] = hallway[i]
              calls.append(play(hc, *rms, cost + ((m + abs(pos_to_go - i)) * cost_lookup[hallway[i]])))
          else:
            flag = True
            for k in range(i - 1, pos_to_go - 1, -1):
              if hallway[k] != 0:
                flag = False
                break
            if flag:
              hc[i] = 0
              room_to_go[ind] = hallway[i]
              calls.append(play(hc, *rms, cost + ((m + abs(pos_to_go - i)) * cost_lookup[hallway[i]])))
            
    return min(calls or [10**10])

play([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['B', 'D'], ['A', 'C'], ['A', 'B'], ['D', 'C'], 0)
print('First part:', least_cost)

Score = namedtuple('Score', 'dist index node prev edge')                                      

room_lookup = {
  'A': 0,
  'B': 1,
  'C': 2,
  'D': 3
}

class Dijkstra(dict):                                                                        
    def __init__(self, node, neighbors, maxitems=None, maxdist=None, target=None):
      cnt = itt.count()                                                                    
      self[node] = Score(0, next(cnt), node, None, None)                                       
      seen = self                                                                          
      heap = [seen[node]]
      visited = set()
                                                                                            
      for s in self._elements(heap, visited, target):
        seen[s.node] = s
        visited.add(s.node)
        for d, m, edge in neighbors(s.node):
          t = seen.get(m, None)
          if t and (t.dist <= d + self.threshold):
            continue
          seen[m] = Score(
            d + self.threshold, next(cnt), m, s.node, edge)
          hq.heappush(heap, seen[m])
      self.root = node
 
    def _heapiter(self, heap):                                                                          
      while heap:                                                                              
        s = hq.heappop(heap)
        self.threshold = s.dist
        yield s
 
    def _elements(self, heap, visited,  target):
      seq = (x for x in self._heapiter(heap) if x.node not in visited)
      seq = itt.takewhile((lambda x: x.node != target), seq)
      return seq

    def rev_path_to(self, node):
      s = self[node]
      while s:
        yield s.node
        s = self.get(s.prev, None)
 
init = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), ('B', 'D', 'D', 'D'), ('A', 'C', 'B', 'C'), ('A', 'B', 'A', 'B'), ('D', 'A', 'C', 'C'))
target = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), ('A', 'A', 'A', 'A'), ('B', 'B', 'B', 'B'), ('C', 'C', 'C', 'C'), ('D', 'D', 'D', 'D'))

def build_hallway(hw, ind, c):
  res = ()
  for i in range(len(hw)):
    if i != ind:
      res += (hw[i],)
    else:
      res += (c,)
  return res

def build_rooms(rooms, i, j, c):
  res = []
  for k in range(len(rooms)):
    tmp = ()
    for l in range(len(rooms[i])):
      if i == k and l == j:
        tmp += (c,)
      else:
        tmp += (rooms[k][l],)
    res.append(tmp)
  return res

def build_new_node(hallway, pi, rooms, i, out_ind, ind):
  new_hallway = build_hallway(hallway, pi, rooms[i][ind])
  r1, r2, r3, r4 = build_rooms(rooms, i, ind, 0)
  new_node = (new_hallway,) + (r1,) + (r2,) + (r3,) + (r4,)
  cost = (ind + 1 + abs(out_ind - pi)) * cost_lookup[rooms[i][ind]]
  return (cost, new_node, None)

def gen_neighbors(node):
  res = []
  rooms = [node[1], node[2], node[3], node[4]]
  hallway = node[0]

  # moves from side room to the hallway
  for i in range(len(rooms)):
    if rooms[i] == (0, 0): continue
    possible_indexes = []
    out_ind = rpos_lookup[i]
    k = out_ind - 1
    while k >= 0 and hallway[k] == 0:
      if k not in out_indexes:
        possible_indexes.append(k) 
      k -= 1

    k = out_ind + 1
    while k < len(hallway) and hallway[k] == 0:
      if k not in out_indexes:
        possible_indexes.append(k)
      k += 1

    for pi in possible_indexes:
      if rooms[i][0] != 0 and rooms[i] != pairs[i] and hallway[out_ind] == 0:
        res.append(build_new_node(hallway, pi, rooms, i, out_ind, 0))
      elif rooms[i][0] == 0 and rooms[i][1] != 0 and hallway[out_ind] == 0 and rooms[i][1:] != pairs[i][1:]:
        res.append(build_new_node(hallway, pi, rooms, i, out_ind, 1))
      elif rooms[i][0] == 0 and rooms[i][1] == 0 and rooms[i][2] != 0 and hallway[out_ind] == 0 and rooms[i][2:] != pairs[i][2:]:
        res.append(build_new_node(hallway, pi, rooms, i, out_ind, 2))
      elif rooms[i][0] == 0 and rooms[i][1] == 0 and rooms[i][2] == 0 and rooms[i][3] != 0 and hallway[out_ind] == 0 and rooms[i][3:] != pairs[i][3:]:
        res.append(build_new_node(hallway, pi, rooms, i, out_ind, 3))

  # moves from hallway into a side room
  for i in range(len(hallway)):
    if hallway[i] != 0:
      pos_to_go = pos_lookup[hallway[i]]     
      room_to_go = rooms[room_lookup[hallway[i]]]
      four_empty = room_to_go[0] == 0 and room_to_go[1] == 0 and room_to_go[2] == 0 and room_to_go[3] == 0
      three_empty = room_to_go[0] == 0 and room_to_go[1] == 0 and room_to_go[2] == 0 and room_to_go[3] == hallway[i]
      two_empty = room_to_go[0] == 0 and room_to_go[1] == 0 and room_to_go[2] == hallway[i] and room_to_go[3] == hallway[i]
      one_empty = room_to_go[0] == 0 and room_to_go[1] == hallway[i] and room_to_go[2] == hallway[i] and room_to_go[3] == hallway[i]
      if four_empty:
        ind = 3
      elif three_empty:
        ind = 2
      elif two_empty:
        ind = 1
      else:
        ind = 0
      m = ind + 1
      if any([four_empty, three_empty, two_empty, one_empty]):
        d = 1
        if pos_to_go < i:
          d = -1

        flag = True
        for k in range(i + d, pos_to_go + d, d):
          if hallway[k] != 0:
            flag = False
            break

        if flag:
          new_hallway = build_hallway(hallway, i, 0)
          r1, r2, r3, r4 = build_rooms(rooms, room_lookup[hallway[i]], ind, hallway[i])
          new_node = (new_hallway,) + (r1,) + (r2,) + (r3,) + (r4,)
          cost = (m + abs(pos_to_go - i)) * cost_lookup[hallway[i]]
          res.append((cost, new_node, None))
  
  for el in res:
    yield el

d = Dijkstra(init, gen_neighbors, target=target)

final_cost = None
for k in d.rev_path_to(target):
  final_cost = d[k].dist
  break

print('Second part:', final_cost)
