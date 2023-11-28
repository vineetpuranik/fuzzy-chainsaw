# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root passed is None then return 0
        if root is None:
            return 0
        
        # root depth will be considered as 1
        # the max depth will correspond 1 + depth of left subtree or right subtree whichever is greater. This can be done recursively.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        