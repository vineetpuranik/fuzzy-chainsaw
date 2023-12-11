# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # lowest common ancestor
        # lowest node in T that has both p and q as descendants
        # a node can be a descendant of itself
        # all node values are unique. p and q will exist in the binary search tree
        # there will be atleast 2 nodes in the tree and atmost 0.1 million nodes
        
        
        # if current node is equal to either p or q then we will return the current node as the lowest common ancestor
        if root.val == p.val or root.val == q.val:
            return root
        
        # if p and q are both less than current node.val that means 
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # if p and q are both greater than current node.val that means
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # if we reach here that means the current node is the lowest common ancestor
        return root
            
        
        
        
        
        
        
