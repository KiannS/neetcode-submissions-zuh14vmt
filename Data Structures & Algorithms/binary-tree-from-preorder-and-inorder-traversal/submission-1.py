# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        location_preorder = {}
        location_inorder = {}

        for i in range (len(preorder)):
            location_preorder[preorder[i]] = i
            location_inorder[inorder[i]] = i
    
        def tree(i: List[int], pidx: int):
            temp = TreeNode()
            if not i:
                return None
            if len(i) == 1:
                temp.val = preorder[pidx]
                return temp
            
            root = findRoot(preorder[pidx], i)

            temp.val = preorder[pidx]
            left  = i[:root]
            right = i[root + 1:]

            temp.left  = tree(left, pidx + 1)
            temp.right = tree(right, pidx + root + 1)
            return temp

        def findRoot(root: int, nums: List[int]):
            for i in range(len(nums)):
                if nums[i] == root:
                    return i
            return -1

        return tree(inorder, 0)
        
               