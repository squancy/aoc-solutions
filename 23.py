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

least_cost = 10**10

def play(hallway, room1, room2, room3, room4, cost):
  global least_cost

  if cost >= least_cost:
    return cost

  if room1 == ['A', 'A'] and room2 == ['B', 'B'] and room3 == ['C', 'C'] and room4 == ['D', 'D']:
    print('YESS', cost)
    if cost < least_cost:
      least_cost = cost
    return cost 
  else:
    # moves out of a room into the hallway
    rooms = [room1, room2, room3, room4]
    calls = []
    #print(hallway, room1, room2, room3, room4)
    for i in range(len(rooms)):
      cur_room = [x for x in rooms[i]]
      possible_indexes = []
      if hallway[step_out[i]] == 0:
        possible_indexes.append(step_out[i]) 
        k = step_out[i] - 1
        while k >= 0 and hallway[k] == 0:
          possible_indexes.append(k)
          k -= 1
      if hallway[step_out[i + 1]] == 0:
        possible_indexes.append(step_out[i + 1]) 
        k = step_out[i + 1] + 1
        while k < len(hallway) - 1 and hallway[k] == 0:
          possible_indexes.append(k)
          k += 1
      for pi in possible_indexes:
        if rooms[i][0] != 0 and rooms[i] != ordered_rooms[i] and hallway[rpos_lookup[i]] == 0:
          cur_room[0] = 0
          hc = [x for x in hallway]
          hc[pi] = rooms[i][0]
          rms = [[x for x in cur_room] if j == i else [y for y in rooms[j]] for j in range(4)]
          #print(hallway, rooms, '->', hc, rms)
          calls.append(play(hc, *rms, cost + (1 + abs(pi - rpos_lookup[i])) * cost_lookup[hc[pi]]))
        elif rooms[i][0] == 0 and rooms[i][1] != 0 and rooms[i][1] != ordered_rooms[i][1] and hallway[rpos_lookup[i]] == 0:
          cur_room[1] = 0
          hc = [x for x in hallway]
          hc[pi] = rooms[i][1]
          rms = [[x for x in cur_room] if j == i else [y for y in rooms[j]] for j in range(4)]
          #print(hallway, rooms, '->', hc, rms)
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
print(least_cost)
