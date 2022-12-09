from collections import defaultdict

instr = [[x.split(' ')[0], int(x.split(' ')[1])] for x in open('9.txt').readlines()]

def is_HT_nb(tail_pos, head_pos):
  arr = []
  for i in range(-1, 2):
    for j in range(-1, 2):
      arr.append([head_pos[0] + i, head_pos[1] + j])
  return tail_pos in arr

def solve(instr, num_of_knots):
  visited = defaultdict(tuple)
  knots = [[0, 0] for i in range(num_of_knots)]
  visited[(0, 0)] = 1
  for d, n in instr:
    for i in range(n):
      if d == 'R':
        knots[0][0] += 1
      elif d == 'L':
        knots[0][0] -= 1
      elif d == 'U':
        knots[0][1] -= 1
      else:
        knots[0][1] += 1

      for i in range(1, len(knots)):
        if not is_HT_nb(knots[i], knots[i - 1]):
          if knots[i - 1][0] == knots[i][0]:
            knots[i][1] += 1 if knots[i - 1][1] > knots[i][1] else -1
          elif knots[i - 1][1] == knots[i][1]:
            knots[i][0] += 1 if knots[i - 1][0] > knots[i][0] else -1
          else:
            for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
              tc = [knots[i][0] + a, knots[i][1] + b]
              if is_HT_nb(tc, knots[i - 1]):
                knots[i] = tc
                break
          visited[tuple(knots[-1])] = 1
  return visited

print('First part:', len(solve(instr, 2)))
print('Second part:', len(solve(instr, 10)))
