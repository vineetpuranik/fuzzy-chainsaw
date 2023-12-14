from typing import List
import unittest


class MaxBinaryHeap:

    #constructor
    def __init__(self):
        self.values = []
    

    def insert(self, v: int):
        # strategy insert at athe end and then bubble up to the right spot

        #insert at the end
        self.values.append(v)

        #bubbling up needs to be done only if we have more than 1 element in our heap
        if len(self.values) > 1 :
            currentNode = len(self.values) - 1

            while currentNode > 0:
                #get the parent node of the current node
                parentNode = (currentNode - 1) // 2

                #if currentNode is greater than parentNode then swap both the values
                if self.values[currentNode] > self.values[parentNode]:
                    temp = self.values[currentNode]
                    self.values[currentNode] = self.values[parentNode]
                    self.values[parentNode] = temp
                    currentNode = parentNode

                # else the currentNode is at a correct position and hence we exit
                else:
                    break

    # extract the maximum value from the max binary heap
    def extractMax(self) -> int:
        # remove value at root
        # move last element to the start of the heap
        # Find the right position of the root element now 

        #if heap is empty return -1
        if len(self.values) == 0:
            return -1

        # if we reach here this means there is at least 1 element in the heap
        # the max element will be the element at index 0 in our heap
        result = self.values[0]

        # we need to now remove the max element from the heap -> move the last element to 0th index -> find the accurate position of the 0th element
        if len(self.values) > 1:

            # remove the last element from the heap
            last_element = self.values.pop()

            # overwrite the first element with the last element and in this way we are moving the last element to the beginning of the heap
            self.values[0] = last_element

            # find the correct position of the element
            currentNode = 0

            while True:
                left_child = (2 * currentNode) + 1
                right_child = (2 * currentNode) + 2
                swap = None

                #check if left child is bigger    
                if left_child < len(self.values):
                    if self.values[left_child] > self.values[currentNode]:
                        swap = left_child        

                #check if right child is bigger
                if right_child < len(self.values):
                    # if right is bigger than left
                    if (swap is None and self.values[right_child] > self.values[currentNode]) or (swap is not None and self.values[right_child] > self.values[left_child]):
                        swap = right_child

                if swap is None:
                    break

                temp = self.values[currentNode]
                self.values[currentNode] = self.values[swap]
                self.values[swap] = temp
                currentNode = swap

        # there is only 1 entry in the heap and hence we will pop it leaving our heap empty
        else:
            self.values.pop()
    
        return result


class TestMaxBinaryHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MaxBinaryHeap()

    def test_insert(self):
        self.heap.insert(10)
        self.heap.insert(20)
        self.heap.insert(5)
        self.assertEqual(self.heap.values[0], 20, "The max element should be at the root.")

    def test_extract_max(self):
        for value in [10, 20, 5]:
            self.heap.insert(value)
        max_value = self.heap.extractMax()
        self.assertEqual(max_value, 20, "Extracted maximum value should be 20.")
        self.assertEqual(self.heap.values[0], 10, "New max value should be 10 after extraction.")

    def test_extract_max_empty_heap(self):
        self.assertEqual(self.heap.extractMax(), -1, "Extracting from an empty heap should return -1.")

    def test_sequential_inserts_and_extracts(self):
        values = [15, 22, 9, 33, 17]
        sorted_values = sorted(values, reverse=True)

        for value in values:
            self.heap.insert(value)

        extracted_values = []
        while len(self.heap.values) > 0:
            extracted_values.append(self.heap.extractMax())

        self.assertEqual(extracted_values, sorted_values, "Extracted values should be in descending order.")

if __name__ == '__main__':
    unittest.main(verbosity=2)