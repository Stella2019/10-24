import collections

class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __repr__(self):
    n = self
    ret = ''
    while n:
      ret += str(n.val) + ' '
      n = n.next
    return ret


class Solution(object):
  def removeZeroSumSublists(self, node):
    sumToNode = collections.OrderedDict()
    sum = 0
    dummy = Node(0)
    dummy.next = node
    n = dummy
    while n:
      sum += n.val
      if sum not in sumToNode:
        sumToNode[sum] = n
      else:
        prev = sumToNode[sum]
        prev.next = n.next
        while list(sumToNode.keys())[-1] != sum:
          sumToNode.popitem()
      n = n.next
    return dummy.next


# 3, 1, 2, -1, -2, 4, 1
n = Node(3)
n.next = Node(1)
n.next.next = Node(2)
n.next.next.next = Node(-1)
n.next.next.next.next = Node(-2)
n.next.next.next.next.next = Node(4)
n.next.next.next.next.next.next = Node(1)
print(Solution().removeZeroSumSublists(n))
# 3, 4, 1
