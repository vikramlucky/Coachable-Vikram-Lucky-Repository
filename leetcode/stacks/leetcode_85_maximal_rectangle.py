'''
Leetcode 85 Maximal Rectangle

Problem Statement:
-> Given a rows x cols binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],
                 ["1","0",|"1","1","1"|],
                 ["1","1",|"1","1","1"|],
                 ["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

'''
from typing import List


class Solution:
    '''Solutio Class'''

    def get_next_left_and_right_min(self, arr):
        '''Helper function'''
        n = len(arr)
        stack = []
        next_min_right = [n] * n
        next_min_left = [-1] * n

        for idx, n in enumerate(arr):
            while len(stack) > 0 and arr[stack[-1]] > n:
                next_min_right[stack.pop()] = idx
            next_min_left[idx] = stack[-1] if len(stack) > 0 else -1
            stack.append(idx)
        return (next_min_right, next_min_left)

    def get_max_area(self, arr):
        '''Helper function 2'''

        area = 0
        next_min_right, next_min_left = self.get_next_left_and_right_min(arr)

        for idx, n in enumerate(arr):
            w = next_min_right[idx] - next_min_left[idx] - 1
            area = max(area, w * n)

        return area

    def maximal_rectangle(self, matrix: List[List[str]]) -> int:
        '''Main function'''

        if not matrix or not matrix[0]:
            return 0

        h = [0] * len(matrix[0])
        ans = 0
        for _, row in enumerate(matrix):
            for j, val in enumerate(row):

                if val == '1':
                    h[j] += 1
                else:
                    h[j] = 0

            ans = max(ans,self.get_max_area(h))
        return ans
