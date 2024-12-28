'''
Leetcode 907. Sum of Subarray Minimums
Given an array of integers arr, find the sum of min(b), 
where b ranges over every (contiguous) subarray of arr. 
Since the answer may be large, return the answer modulo 109 + 7.


Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444

Approach:

Optimal solution:
	1.	Identify Ranges:
	    •	For each element in arr, find:
	    •	PSE: How far left the current element can extend while remaining the smallest.
	    •	NSE: How far right the current element can extend while remaining the smallest.
	    •	Use > for PSE and >= for NSE to handle duplicates correctly.

	2.	Calculate Contributions:
	    •	Each element contributes:
            arr[i] * (distance to left) * (distance to right)
	    •	Sum up contributions for all elements.
         
	3.	Modulo Operation:
	    •	Use modulo 10^9 + 7 to handle large numbers.
'''

from collections import deque
from typing import List
class Solution:
    '''Solution class'''

    def get_right_min(self, arr: List[int]) -> list:
        '''Given arr this function return next smaller element to the right'''
        n = len(arr)
        right_min = [n for x in arr]
        stack = deque()

        for idx, num in enumerate(arr):

            while len(stack) and arr[stack[-1]] > num:
                i = stack.pop()
                right_min[i] = idx
            stack.append(idx)

        return right_min

    def get_left_min(self, arr: List[int]) -> list:
        '''Return previous smallest element'''

        n = len(arr)
        left_min = [-1 for x in arr]
        stack = deque()

        for idx in range(n - 1,  -1, -1):
            num = arr[idx]
            while len(stack) and arr[stack[-1]] >= num:
                i = stack.pop()
                left_min[i] = idx
            stack.append(idx)

        return left_min


    def sum_subarray_mins(self, arr: List[int]) -> int:
        '''main functions returns the answer'''

        tot_sum = 0
        mod = 10 ** 9 + 7

        right_min = self.get_right_min(arr)
        left_min = self.get_left_min(arr)
        print(right_min, left_min)
        for idx, n in enumerate(arr):

            sub_arr_size = (right_min[idx] - idx) * (idx - left_min[idx])
            tot_sum = (tot_sum + sub_arr_size * n) % mod

        return tot_sum
