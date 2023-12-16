# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # important 
        # if subRoot is None then we return True since a null tree will always be a subTree of a valid tree
        if subRoot is None:
            return True
        
        # root is None but subRoot is not None then we return False
        if root is None and subRoot:
            return False
        
        # if root and subRoot are same Trees then return True
        if self.isSameTree(root, subRoot):
            return True
        
        # if not then check if root.left and subRoot are subtrees or root.right and subRoot are subtrees
        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if a and b is None: 
                return False
            
            if b and a is None:
                return False
            
            if a is None and b is None:
                return True
            
            if a.val != b.val:
                return False
            
            return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
    
    
    
        
        
        
        
       
        