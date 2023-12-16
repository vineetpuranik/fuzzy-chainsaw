class MinHeap:
    # in a min heap the root will be less than both the left child and the right child
    # after the root an element is added to the left side first and then to the right side
    # heap consumes optimal space

    def __init__(self):
        # for heaps storing the elements in the form of a list is the most efficient way
        # every node can have at most 2 children; a left child and a right child
        # for a node n the left child is located at an index 2n + 1 and the right child is located
        # at an index 2n + 2
        # for a node n the parent is located at an index floor (n - 1) // 2
        self.values = []

    def push(self, val: int) -> None:
        # general idea : append the new element at the end of the heap and bubble up to its correct position

        # if the heap is currently empty then, we will directly add the value and return
        if len(self.values) == 0:
            self.values.append(val)
            return                           

        # add the element to the end of the heap
        self.values.append(val)

        # current index of the newly added val
        currentIndex = len(self.values) - 1

        # bubble up the element to its correct position

        while currentIndex > 0 : 
            # calculate the parent index
            parentIndex = (currentIndex - 1) // 2

            # if element at currentIndex is less than element at the parentIndex then swap
            if self.values[currentIndex] < self.values[parentIndex]:
                #swap the elements
                temp = self.values[currentIndex]
                self.values[currentIndex] = self.values[parentIndex]
                self.values[parentIndex] = temp

                # update the currentIndex to the parentIndex
                currentIndex = parentIndex

            # else the element is already at its accurate position in the heap
            # break the loop    
            else:
                break

        return


    def pop(self) -> int:
        # return the element at the top or root of the heap
        # general idea : remove the element at the top of the heap by overwriting it with the element at the last index
        # find the accurate position of the new root element now


        # if the heap is empty return -1 
        if len(self.values) == 0:
            return -1

        # if there are more than 1 elements in the heap
        if len(self.values) > 1:
            # store the root element in a variable and this will be the result we return
            result = self.values[0]

            # remove the last element from the heap and overwrite the first element with the last element
            # this will make sure that we are moving the value at the end of the heap to the front of the heap efficiently
            last_element = self.values.pop()
            self.values[0] = last_element

            # now, we need to find the correct position of the element at the root
            # declare swap which will be used to identify the correct position
           
            currentIndex = 0

            # we will continue this loop until we find the accurate position
            # the loop will be terminated by a condition executing inside the loop
            while True:

                # calculate the left and right child indices
                leftChildIndex = (2* currentIndex) + 1
                rightChildIndex = (2* currentIndex) + 2
                swap = None

                # left child index is in bounds
                if (leftChildIndex < len(self.values)):

                    # if left child value is less then set swap to left child index
                    if (self.values[leftChildIndex] < self.values[currentIndex]):
                        swap = leftChildIndex

                    # check if right child is in bounds
                    if (rightChildIndex < len(self.values)):
                        # there are 2 cases here
                        # if swap is none and rightChild < currentIndex value
                        # or if swap is not none and rightChild < leftChild

                        if (swap is None and self.values[rightChildIndex] < self.values[currentIndex]) or (swap is not None and self.values[rightChildIndex] < self.values[leftChildIndex]):
                            swap = rightChildIndex


                    # if swap is none after checking both the left and right children
                    # this means the parent is at the correct position and we can break out from the loop
                    if swap is None:
                        break

                    # else swap the values and update the currentIndex
                    temp = self.values[currentIndex]
                    self.values[currentIndex] = self.values[swap]
                    self.values[swap] = temp

                    currentIndex = swap

                #left child index is out of bounds also implies that right child index will be out of bounds
                # we break out from the loop
                else:
                    break    

            return result

        # if there is only 1 element in the heap
        else:
            # pop the only element in the heap and store it in a variable
            result = self.values.pop()
            # list.pop() in python removes the last element from the list
            return result



        

    def top(self) -> int:
        # return the smallest element without removing it.

        # if there are no elements in the min heap then return - 1
        if len(self.values) == 0:
            return -1

        # there are elements in the heap hence top will return the element at the 0th index which
        # will be the root element and the smallest element in the heap
        return self.values[0]    
        

    def heapify(self, nums: List[int]) -> None:

        for i in range(len(nums)):
            self.push(nums[i])

        
        
