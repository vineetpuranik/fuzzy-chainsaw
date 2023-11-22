# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if the current node in both p and q is none
        if p is None and q is None:
            return True

        # if p is none and q is not none
        if p is None and q is not None:
            return False    
        
        # if p is not none and q is None
        if p is not None and q is None:
            return False

        #if values for both nodes are different
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)