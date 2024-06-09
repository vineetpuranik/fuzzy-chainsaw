# middle of the linked list
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Linked list
# 1 - 2 - 3 - 4 - 5
# Length of the linked list = 5 since there are 5 elements in the linked list
# middle of the linked list = (length / 2 ) + 1 = 3rd element


# Linked list 
# 1 - 2 - 3 - 4 - 5 - 6
# Length of the linked list = 6 since there are 6 elements in the linked list
# middle of the linked list = (length / 2) + 1 = 4th element

class Solution(object):
    def middleNode(self, head):

        # if there is only 1 element in the linked list then return head as is
        if head.next is None : 
            return head
        
        # calculate the length of the linked list
        list_length = 1
        current = head
        # 1 - 2 - 3 - 4
         
        while current.next is not None:
            list_length += 1
            current = current.next

        middle = (list_length // 2) + 1

        iterator = 1
        while iterator < middle:
            iterator += 1
            head = head.next
            
        return head
    

