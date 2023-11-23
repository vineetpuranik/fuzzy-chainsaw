# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        # create queue for iterating the tree
        q = collections.deque()
        
        # add root to the queue
        q.append(root)
        
        while q:
            node = q.popleft()
            
            if node is not None:
                #swap left and right children
                temp = node.left
                node.left = node.right
                node.right = temp
                
                #add left and right children to the queue
                q.append(node.left)
                q.append(node.right)
        
        
        return root