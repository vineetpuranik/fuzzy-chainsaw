import unittest
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = intervals.sort(key = lambda i : i[0])
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_true_test_case(self):
        self.assertTrue(self.solution.canAttendMeetings([[1, 5], [9, 11]]))

    def test_false_test_case(self):
        self.assertFalse(self.solution.canAttendMeetings([[1, 5], [2, 5]]))


if __name__ == '__main__':
    unittest.main()
