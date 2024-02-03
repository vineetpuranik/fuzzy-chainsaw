# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # the number of nodes in the tree is n
        # there will be atleast 1 node in the tree
        # input k is always less than or equal to the number of nodes in the tree

        vals = []

        def traverse(node):
            if node :
                # check if left node is present. If yes, visit the left node
                if node.left:
                    traverse(node.left)

                # after visiting the left node at the value of the current node to vals
                vals.append(node.val)

                # check if right node is present. If yes, visit the right node
                if node.right:
                    traverse(node.right)

        # call traverse from root
        # 3 
        # 1 -> node.left is None : add 1 to vals : call traverse on node.right
        # 2 -> node.left is None : Add 2 to vals : node.right is None go back to 1
        # 1 will complete execution. add 3 to vals
        # call travserse on node.right 
        # 4 : node.left is None. Add 4 to vals  

        traverse(root)
        return vals[k - 1]

