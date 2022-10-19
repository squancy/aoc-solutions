inp = [x.rstrip() for x in open('inp12.txt').readlines()]

def facing_to_mul(facing):
  return 1 if facing in [0, 1] else -1

def first_part():
  pos = [0, 0]
  facing = 0

  for instr in inp:
    if instr[0] == 'N':
      pos[1] += int(instr[1:]) 
    elif instr[0] == 'S':
      pos[1] -= int(instr[1:]) 
    elif instr[0] == 'E':
      pos[0] += int(instr[1:])
    elif instr[0] == 'W':
      pos[0] -= int(instr[1:])
    elif instr[0] == 'F':
      if facing in [1, 3]:  
        pos[1] += int(instr[1:]) * facing_to_mul(facing)
      else:
        pos[0] += int(instr[1:]) * facing_to_mul(facing)
    elif instr[0] in ['L', 'R']:
      x = (int(instr[1:]) % 360) // 90
      facing += x if instr[0] == 'L' else -x
      facing %= 4
      if facing < 0: facing += 4
  return abs(pos[0]) + abs(pos[1])

def second_part():
  ship_pos = [0, 0]
  waypoint_pos = [10, 1]
  for instr in inp:
    if instr[0] == 'N':
      waypoint_pos[1] += int(instr[1:])
    elif instr[0] == 'S':
      waypoint_pos[1] -= int(instr[1:])
    elif instr[0] == 'E':
      waypoint_pos[0] += int(instr[1:])
    elif instr[0] == 'W':
      waypoint_pos[0] -= int(instr[1:])
    elif instr[0] == 'L':
      for i in range(int(instr[1:]) // 90):
        waypoint_pos = [-waypoint_pos[1], waypoint_pos[0]]
    elif instr[0] == 'R':
      for i in range(int(instr[1:]) // 90):
        waypoint_pos = [waypoint_pos[1], -waypoint_pos[0]]
    elif instr[0] == 'F':
      ship_pos[0] += waypoint_pos[0] * int(instr[1:])
      ship_pos[1] += waypoint_pos[1] * int(instr[1:])
  return abs(ship_pos[0]) + abs(ship_pos[1])

print('First part:', first_part())
print('Second part:', second_part())
