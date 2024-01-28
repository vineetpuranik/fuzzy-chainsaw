#define a Node for the linked list 
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    # initialize head, tail and length
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0    


    def get(self, index: int) -> int:
        # if there are no elements in the linked list or 
        # the input index is greater than the elements in the linked list
        # we will return -1
        # 0 1 3 : length = 3, index = 2
        if self.length == 0 or index >= self.length:
            return -1

        current = self.head
        counter = 0

        # index = 0 ; while loop will not execute and current.val will be returned
        # index = 1 ; while loop will be executed once and will return the val of the second node
        while counter < index:
            current = current.next 
            counter += 1   

        return current.val

    def insertHead(self, val: int) -> None:
        # create a new node from the val passed
        node = Node(val)

        # if elements exist in the linked list
        if self.length > 0 :
            currentHead = self.head
            self.head = node
            self.head.next = currentHead

        # if there are no elements in the linked list    
        else:
            # set head and tail as the new node    
            self.head = node
            self.tail = node

        # increment the length
        self.length += 1


    def insertTail(self, val: int) -> None:
        # create a new node from the val passed
        node = Node(val)

        # if elements exist in the linked list
        if self.length > 0 :
            currentTail = self.tail
            self.tail = node
            currentTail.next = node

        # if there are no elements in the linked list    
        else:
            # set head and tail as the new node    
            self.head = node
            self.tail = node

        # increment the length
        self.length += 1

    def remove(self, index: int) -> bool:

        # check if index is out of bounds
        if self.length == 0 or index >= self.length:
            return False

        # 0 1 2
        # 0 head
        # 1 mid
        # 2 tail

        # remove 0 : 1 head 2 tail 
        # remove 1 : 0 head 2 tail # need prev and next in order to update the links correct
        # prev.next = current.next
        # remove 2 : 0 1 : update 1 as the new tail , prev = self.tail
        # input index could lead to removal from head, tail or middle of the linked list

        # remove from head
        if index == 0: 
            self.head = self.head.next
        
        # remove from tail or remove from middle
        # 0 1 2 
        else:
            prev = None
            current = self.head
            counter = 0
            # index = 2 
            # counter = 0 ; prev = None; current = 0
            # counter = 1 ; prev = 0; current = 1
            # counter = 2 ; prev = 1; current = 2
            # counter = 3 ; exit while loop
            while counter < index :
                prev = current
                current = current.next
                counter += 1

            prev.next = current.next

            # update tail if we removed the last element
            if index == self.length - 1:
                self.tail = prev

        
        # decrement the length
        self.length = self.length - 1

        # if length == 1 then update the head and tail
        if self.length == 1:
            self.tail = self.head

        return True

    def getValues(self) -> List[int]:
        result = []
        # 0, 1, 2
        if self.length > 0:
            current = self.head
            counter = 0
            while counter < self.length:
                result.append(current.val)
                current = current.next
                counter += 1

        return result
