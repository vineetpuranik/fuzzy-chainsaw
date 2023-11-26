from typing import List

class Solution:

    def mergesort(self, a: List[int]) -> List[int]:
        if len(a) > 1:
            mid = len(a) // 2  # Correct calculation of mid

            left_half = self.mergesort(a[:mid])  # Left half of the array
            right_half = self.mergesort(a[mid:])  # Right half of the array

            # This is where you would merge the two halves
            # Assuming merge() is a function that you will implement
            return self.merge(left_half, right_half)    
        else:
            return a

    
    def merge(self, x :List[int], y :List[int]) -> List[int]:
        if not x :
            return y
        
        if not y :
            return x

        if x[0] <= y[0]:
            return [x[0]] + self.merge(x[1:], y)

        else:
            return [y[0]] + self.merge(x, y[1:])


'''
mergesort Method:

Splits the input list a into two halves (left and right) recursively until the length of each sublist is less than or equal to 1.
Calls the merge method to combine these halves back into a sorted list.
merge Method:

Merges two sorted lists (x and y) into a single sorted list.
Handles cases where one of the lists is empty.
Recursively merges elements from the two lists, selecting the smaller element from the front of either list at each step.
'''

sol = Solution()
sorted_array = sol.mergesort([34, 7, 23, 32, 5, 62])
print(sorted_array)
sorted_array = sol.mergesort([2, 1])
print(sorted_array)
sorted_array = sol.mergesort([3, 100])
print(sorted_array)
