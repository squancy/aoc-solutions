import re

lines = [x.rstrip() for x in open('inp8.txt').readlines()]

def first_part(lines):
  string_code = 0
  in_memory = 0
  for line in lines:
    string_code += len(line) 
    line = re.sub(r'\\\\|\\"|\\x[0-9a-f]{2}', '_', line)
    in_memory += len(line) - 2
  return string_code - in_memory

def second_part(lines):
  old_string_code = 0
  new_string_code = 0
  for line in lines:
    old_string_code += len(line)
    line = re.sub(r'"|\\', '__', line)
    new_string_code += len(line) + 2
  return new_string_code - old_string_code

print('First part:', first_part(lines))
print('Second part:', second_part(lines))
