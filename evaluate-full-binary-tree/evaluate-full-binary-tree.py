# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        # full binary tree root is given
        # leaf nodes = nodes with no children left and right are None.
        # non leaf nodes are nodes with atleast one child. 
        # leaf nodes have a value of either 0 or 1 where 0 represents False and 1 represents True
        # non leaf nodes have either the value 2 or 3 where 2 represents OR and 3 represents AND
        # if node is a leaf node then evaluation is the value of the node i.e. True or False.
        # otherwise evaluate the the node's two children and apply the boolean operation of its value with the children's evaluation
        # return boolean result of evaluating the root node. 

      
        # A full binary tree is a binary tree where each node has either 0 or 2 children. 
        # A leaf node is a node that has zero children. 

      
        # base case
        # current node has no children
        if root.left is None and root.right is None:
            if root.val == 0 : 
                return False
            return True    

      
        # if we reach here that means left and right child of the current node exists
        if root.val == 2 :
            # we need to perform OR operation on left and right children
            # first recursively evaluate the boolean values of left and right children
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        if root.val == 3 :
             # we need to perform AND operation on left and right children
            # first recursively evaluate the boolean values of left and right children
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)


        # visiting each node of the tree once. hence time complexity is O(n)    
