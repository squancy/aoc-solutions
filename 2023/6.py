import re
import math

def parse_input():
  lines = [re.sub(r"\s+", " ", x.strip()) for x in open('6.txt').readlines()]
  time = [int(x) for x in lines[0].split(' ')[1:]]
  dist = [int(x) for x in lines[1].split(' ')[1:]]
  return time, dist

def parse_input_2():
  lines = [re.sub(r"\s+", " ", x.strip()) for x in open('6.txt').readlines()]
  time = int(lines[0].replace('Time: ', '').replace(' ', ''))
  dist = int(lines[1].replace('Distance: ', '').replace(' ', ''))
  return [[time], [dist]]

def solve(inp):
  prod = 1
  for i in range(len(inp[0])):
    y = inp[0][i]
    x = inp[1][i]
    x1 = math.floor((y - (y ** 2 - 4 * x) ** 0.5) / 2 + 1)
    x2 = math.ceil((y + (y ** 2 - 4 * x) ** 0.5) / 2 - 1)
    prod *= x2 - x1 + 1
  return prod

inp = parse_input()
print('First part:', solve(inp))
inp_2 = parse_input_2()
print('Second part:', solve(inp_2))
