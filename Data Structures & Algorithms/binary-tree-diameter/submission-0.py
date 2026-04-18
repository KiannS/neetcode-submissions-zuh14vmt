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
            left = 0
            right = 0
            if root.left:
                left = computeLongest(root.left)
            if root.right:
                right = computeLongest(root.right)
            longest = max(longest, left + right)
            return max(left, right) + 1
        computeLongest(root)
        return longest
            
