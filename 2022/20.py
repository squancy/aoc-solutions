class Node:
  def __init__(self, v, prev = None, nx = None):
    self.v = v
    self.prev = prev
    self.next = nx

D_KEY = 811589153

def read_nodes(mul):
  f = open('20.txt').readlines()
  nodes = [Node(int(x.strip()) * mul) for i, x in enumerate(f)]
  zero_node = None
  for i, node in enumerate(nodes):
    if node.v == 0: zero_node = node
    if i == 0:
      node.prev = nodes[-1]
      node.next = nodes[i + 1]
    elif i == len(nodes) - 1:
      node.prev = nodes[i - 1]
      node.next = nodes[0]
    else:
      node.prev = nodes[i - 1]
      node.next = nodes[i + 1]
  return nodes, zero_node

def mix(nodes):
  for node in nodes:
    if node.v == 0: continue
    for i in range(abs(node.v) % (len(nodes) - 1)):
      p = node.prev
      n = node.next
      if node.v > 0:
        node.next = node.next.next
        node.prev = n
        p.next = node.prev
        n.next = node
        n.prev = p
        node.next.prev = node
      else:
        node.next = node.prev 
        node.prev = node.prev.prev
        p.next = n
        p.prev = node
        n.prev = p
        node.prev.next = node

def calc_res(zero_node):
  summa = 0
  for n in [1000, 2000, 3000]:
    cn = zero_node
    for i in range(n):
      cn = cn.next 
    summa += cn.v
  return summa

def first_part(nodes, zero_node):
  mix(nodes)
  return calc_res(zero_node)

def second_part(nodes, zero_node):
  for i in range(10):
    mix(nodes)
  return calc_res(zero_node)

nodes, zero_node = read_nodes(1)
print('First part:', first_part(nodes, zero_node))
nodes, zero_node = read_nodes(D_KEY)
print('Second part:', second_part(nodes, zero_node))
