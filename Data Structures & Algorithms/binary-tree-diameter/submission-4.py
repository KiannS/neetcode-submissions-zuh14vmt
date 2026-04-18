# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        longest = 0 
        def computeLongest(root):
            nonlocal longest
            if not root:
                return 0
            left = 0
            right = 0
            left = computeLongest(root.left)
            right = computeLongest(root.right)
            longest = max(longest, left + right)
            return max(left, right) + 1
        computeLongest(root)
        return longest
            
