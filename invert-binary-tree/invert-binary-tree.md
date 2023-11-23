## Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

## Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

## Algorithm
1. Given root , swap left child with right child. 
2. Add left child and right child to a queue. 
3. Continue step 1 by popping from the queue until the queue is empty.

# Runtime analysis
1. Time complexity : O(n) : since we will visit all the nodes in the tree once.
2. Space complexity : O(n) : since we will add all the nodes to the queue. 