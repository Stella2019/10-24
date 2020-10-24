class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    return self.val


def deepest(node):
  if not node:
    return 0
  return 1 + max(deepest(node.left), deepest(node.right))


def deepest2(node, depth=0):
  if not node:
    return depth + 0

  if not node.left and not node.right:
    return depth + 1

  if not node.left:
    return deepest2(node.right, depth + 1)

  if not node.right:
    return deepest2(node.left, depth + 1)

  return max(deepest2(node.left, depth + 1),
             deepest2(node.right, depth + 1))


#    a
#   / \
#  b   c
# /
# d
#  \
#   e
root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.left.right = Node('e')
root.right = Node('c')

print(deepest2(root))
# 4
