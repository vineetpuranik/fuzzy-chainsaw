# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we can do this in O(n) by using a set
        # to do this in O(1) space we need to use Floyd's algorithm
       
        # start both slow and fast at head
        slow, fast = head, head
        
        # if either of fast or fast.next is None that means we reached the end of the list
        while fast and fast.next:
            # slow will be shifted to the next node
            slow = slow.next
            
            # fast will be shifted to fast.next.next
            fast = fast.next.next

            # if slow and fast both are same that means we have found the cycle
            if slow == fast :
                return True
            

        # if we reach here that means there was no cycle in list
        return False     
        






