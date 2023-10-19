def obj_has_red(obj):
  return 'red' in obj.values()

def add_nums(json):
  s = 0
  if isinstance(json, dict):
    for k in json:
      if isinstance(json[k], int):
        s += json[k]
      elif isinstance(json[k], list) or isinstance(json[k], dict):
        s += add_nums(json[k])
  elif isinstance(json, list):
    for el in json:
      if isinstance(el, int):
        s += el
      elif isinstance(el, list) or isinstance(el, dict):
        s += add_nums(el)
  elif isinstance(json, int):
    s += json
  return s

def add_nums_red(json):
  s = 0
  if isinstance(json, dict) and not obj_has_red(json):
    for k in json:
      if isinstance(json[k], int):
        s += json[k]
      elif isinstance(json[k], list) or (isinstance(json[k], dict) and not obj_has_red(json[k])):
        s += add_nums_red(json[k])
  elif isinstance(json, list):
    for el in json:
      if isinstance(el, int):
        s += el
      elif isinstance(el, list) or (isinstance(el, dict) and not obj_has_red(el)):
        s += add_nums_red(el)
  elif isinstance(json, int):
    s += json
  return s

output_list = eval(open('inp12.txt').readline())
print('First part:', add_nums(output_list))
print('Second part:', add_nums_red(output_list))
