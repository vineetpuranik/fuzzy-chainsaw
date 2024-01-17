# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if tree does not exist
        if not root:
            return []

        results = []

        # for level order traversal a.k.a BFS we will need a queue
        # we will start by adding the root element to the queue
        # at every level we will pop all the elements from that level from the queue
        # at every level we will also keep on adding the left and right children of the elements to the queue.

        queue = collections.deque()
        queue.append(root)

        # we will continue to iterate while we have no elements to look for at the current level
        while queue:
            # queue length at this level will signify the number of elements on this level
            queueLength = len(queue)
            level = [] # list to store the values of all the elements at the current level

            # we will pop all the elements that are present at the current level
            for i in range(queueLength):
                # pop from the queue
                currentNode = queue.popleft()

                # if the current element is not None then we will add the value to level list
                # additionally we will also add the left and right children to the queue

                if currentNode:
                    level.append(currentNode.val)
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)


            # once we have iterated all the elements at the current level we will add level list to results
            if level:
                results.append(level)


        return results


        
