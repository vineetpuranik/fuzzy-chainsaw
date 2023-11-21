import unittest
from typing import List


class Solution: 

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        count = {}
        frequency = [[] for i in range(len(nums) + 1)] # since we will not be using the 0th index of the array : O(n)

        # populate count hashmap / dictionary this takes O(n)
        for n in nums: 
            count[n] = 1 + count.get(n, 0) 

        # this takes O(n)
        # populate the frequency array
        for n, c in count.items(): # key is the number and value is the times that it occurs
            frequency[c].append(n)

        results = []

        #iterate the frequency array starting from the last index
        # This takes O(n) + O(n) since each time the inner loop will go over the elements of the input only once. This is like DFS
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                results.append(n)
                if len(results) == k :
                    return results

             
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual([1, 2], self.solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))

    def test_example_2(self):
        self.assertEqual([1], self.solution.topKFrequent([1], 1))



if __name__ == '__main__':
    unittest.main()



