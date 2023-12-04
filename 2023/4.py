import re

def parse_input():
  c = re.compile('Card\s+\d+:\s+((?:\d+\s*)+)\s+|\s+((?:\d+\s*)+)')
  for line in open('4.txt').readlines():
    s = re.findall(c, line.strip()) 
    print(s)

parse_input()
