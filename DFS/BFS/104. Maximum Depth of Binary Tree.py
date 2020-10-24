"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # Note - Recursion won't work on large trees, due to the limit on stack limit size.
        # Iteration, on the other hand, uses heap space which is limited only by how
        # much memory is in the computer.

        class Node(object):
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        class Solution(object):
            def maxDepth(self, n):
                stack = [(1, n)]

                max_depth = 0
                while len(stack) > 0:
                    depth, node = stack.pop()
                    if node:
                        max_depth = max(max_depth, depth)
                        stack.append((depth + 1, node.left))
                        stack.append((depth + 1, node.right))
                return max_depth

            def maxDepthRecursive(self, n):
                if not n:
                    return 0
                return max(self.maxDepthRecursive(n.left) + 1,
                           self.maxDepthRecursive(n.right) + 1)

        n = Node(1)
        n.left = Node(2)
        n.right = Node(3)
        n.left.left = Node(4)

        print(Solution().maxDepth(n))
        # 3

        print(Solution().maxDepthRecursive(n))
        # 3