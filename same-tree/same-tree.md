## Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Constraints
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104


## Idea
Recursively check each node of the binary trees p and q. 
Return false if either : values of the nodes do not match or one of the nodes is None

## Time complexity
Since we are iterating every node of both the input trees once, the runtime is O(p + q)
No new memory is allocated. 

## Examples

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2,1], q = [1,1,2]
Output: false

Input: p = [1,2], q = [1,null,2]
Output: false


