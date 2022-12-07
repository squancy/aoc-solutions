lines = [x.rstrip() for x in open('7.txt').readlines()]

class Tree:
  def __init__(self, typ, size, parent):
    self.typ = typ
    self.size = size
    self.parent = parent
    self.children = []

def build_tree(lines):
  root = Tree('d', 0, None)
  current_node = root
  children = []

  for i in range(len(lines)):
    line = lines[i]
    if line.startswith('$'):
      cmd = line[2:].split(' ')
      if cmd[0] == 'cd':
        if cmd[1] == '/':
          current_node = root
        elif cmd[1] == '..':
          current_node = current_node.parent
        else:
          new_dir = Tree('d', 0, current_node)
          current_node.children.append(new_dir)
          current_node = new_dir
      else:
        children = []
    else:
      if line.startswith('dir'):
        children.append(Tree('d', 0, current_node))
      else:
        children.append(Tree('f', int(line.split(' ')[0]), current_node))
      if i == len(lines) - 1 or lines[i + 1].startswith('$'):
        current_node.children = children
  return root

def traverse(root, dirs):
  if not root.children:
    return root.size
  dirs[root] = 0
  for el in root.children:
    dirs[root] += traverse(el, dirs)
  return dirs[root]

root = build_tree(lines)
dirs = {}
traverse(root, dirs)

def first_part(lines):
  return sum([x for x in dirs.values() if x <= 100000])

def second_part():
  unused_space = 70000000 - dirs[root]
  space_needed = 30000000 - unused_space
  return min([x for x in dirs.values() if x >= space_needed])

print('First part:', first_part(lines))
print('Second part:', second_part())
