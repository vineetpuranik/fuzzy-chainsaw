"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from typing import List
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        #create a hashmap
        inputToClonedNode = {}

        def dfs(node):
            # if the node from the input graph is already cloned and present in the hashmap
            if node in inputToClonedNode:
                return inputToClonedNode[node]

            # create a cloned Node
            clonedNode = Node(node.val)

            # add to the hashmap
            inputToClonedNode[node] = clonedNode

            # call dfs recursively on the neighbors of the input node so that we can clone them as well.
            for n in node.neighbors:
                clonedNode.neighbors.append(dfs(n))

            #return the clonedNode
            return clonedNode

        return dfs(node)

