"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root, direction = ""):
            if not root:
                return 0
            if not root.left and not root.right:
                if direction == "l":
                    return root.val
            left, right = 0, 0
            if root.left:
                left = helper(root.left, "l")
            if root.right:
                right = helper(root.right, "r")

            return left + right
        return helper(root, "")