# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # if head is None
        # No list exists return None
        if head is None:
            return None

        # we will start reversing from the head
        # we will assume there is a None Node that appears before the current head
        # this will be denoted the prev = None
        prev = None

        # current Node will be set to head
        current = head

        # we will run the loop until current is not None
        while current != None:
            # store current.next .This will be the next node in our while loop iteration
            temp = current.next
            # set current.next to prev
            current.next = prev
            # set prev to current
            prev = current
            # set current to the next node we need to iterate
            current = temp


        return prev
