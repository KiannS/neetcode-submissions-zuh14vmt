# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        stack.append((root, root.val))
        res = 0

        while stack:
            curr, best = stack.pop()
            if curr.val >= best:
                res += 1
                best = curr.val
            if curr.right:
                stack.append((curr.right, best))
            if curr.left:
                stack.append((curr.left, best))
            
        return res




        