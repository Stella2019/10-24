from collections import deque

class Node(object):
  def __init__(self, val, children):
    self.val = val
    self.children = children

def levelPrint(node):
  q = deque([node])
  result = ''
  while len(q):
    num = len(q)
    while num > 0:
      node = q.popleft()
      result += str(node.val)
      for child in node.children:
        q.append(child)
      num -= 1
    result += "\n"
  return result

tree = Node('a', [])
tree.children = [Node('b', []), Node('c', [])]
tree.children[0].children = [Node('g', [])]
tree.children[1].children = [Node('d', []), Node('e', []), Node('f', [])]

print(levelPrint(tree))