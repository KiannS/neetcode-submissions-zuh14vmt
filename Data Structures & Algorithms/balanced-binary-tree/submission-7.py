# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        if not root:
            return isBalanced
        def checkLen(root):
            nonlocal isBalanced
            leftLen, rightLen = 0, 0
            if root.left:
                leftLen = checkLen(root.left) + 1
            if root.right:
                rightLen = checkLen(root.right) + 1
            if abs(leftLen - rightLen) > 1:
                isBalanced = False
            return max(leftLen, rightLen)

        checkLen(root)
        return isBalanced

        
        