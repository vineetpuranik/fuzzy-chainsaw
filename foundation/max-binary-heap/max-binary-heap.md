# Binary Heaps
Binary heaps are trees where each node in the tree will have at most 2 children ; a left child and a right child. Hence, the name Binary heaps.
There are 2 types of binary heaps : max binary heaps and min binary heaps. 
In a max binary heap, the parent is always greater than both the left child and right child. Conversely in a min binary heap, the parent is always less than both the left child and the right child. 
When you extract the root element from a max binary heap you are guaranteed to get the highest element in the heap. Conversely, extracting the element at the root from a min binary heap will return the lowest element. 

# Storage
The most efficient way to store binary heap nodes is in the form of an array / list. 
Given a node n in a binary heap. The left child is located at an inded 2n + 1 and the right child is located at an index 2n + 2 consider 0 based indexing. 
Given a node n in a binary heap, the parent node is located at floor(n - 1) / 2

# Max binary heaps
For the implementation we will consider max binary heaps. 

## Insert
heap.append(newElement) -> insert the new element at the end of the heap.
currentIndex = len(heap) - 1
Continue while currentIndex > 0 
    1. calculate the parentIndex = floor(currentIndex - 1) // 2
    2. if heap[currentIndex] > heap[parentIndex]. Swap the two elements and set currentIndex = parentIndex
    3. else the element at currentIndex is at the right location and hence breakout from the loop

Time complexity of insert is O(log n)


## Extract Max
Return the maximum element from the heap is straightforward. We need to however, make sure that maximum element is removed from the heap, the rest of the heap maintains the properties of the max binary heap
1. Set result = heap[0]
2. Remove the last element from the heap. heap.pop()
3. Since we have stored the result , we can directly overwrite heap[0] with the last element. So, now the last element is moved as the first element in the heap. 
4. We need to now find the correct position of the first element. 
5. This is done by checking both the left and right child elements and swapping the first element with the maximum element from the left and right children if both exist. After swapping, we move our current index which initially starts from 0 to the position of the left / rigth child index depending on which one we swapped with and then continue from there. 

Time complexity is O(logn)

