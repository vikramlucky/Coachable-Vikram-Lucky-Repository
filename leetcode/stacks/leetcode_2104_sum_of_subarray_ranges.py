'''Leetcode 2104: VERY VERY IMPORTANT: Ranges and Contribution pattern:
Input = list of ints ex: num = [1, 2, 3]
Output: Return the sum of all subarray ranges of nums: The range of subarray of nums is the 
different between the largest and smallest element in the subarray:

Brute Force: Time: O(n ^ 2):
             Space: O(1)
    - Run a loop i from 0 -> len(nums)
     -> set up: curr_min and curr_max  to nums[i]
     -> Run a inner loop from i + 1 -> len(nums)
        -> Compare and update curr_min and curr_max, with nums[j]
        -> update total_sum = different between curr_max and curr_min
    - Return total_sum


Optimal Solution Using Ranges and contribution monotonic stack pattern:
Time: O(n)
Space: O(n)
	1.	Contribution of Each Element:
	    •	Each element contributes:
	        •	Positively as the maximum of some subarrays.
	        •	Negatively as the minimum of some subarrays.

	2.	Core Idea:
	    •	For each element in the array:
	        •	Determine how many subarrays consider it the maximum.
	        •	Determine how many subarrays consider it the minimum.
	    •	Use this information to calculate its net contribution:
        Contribution =  max contribution - min contribution

	3.	Efficiency:
	    •	Use monotonic stacks to efficiently calculate the count of 
        subarrays where each element is the maximum or minimum.

Approach:

1. Define Contributions

    For an element at index i:
	1.	As Maximum:
	    •	The number of subarrays where nums[i] is the maximum is:
        (distance to previous smaller element) * (distance to next smaller element)

	    •	Formula:
        (max contribution) = nums[i] * (i - prev_greater[i]) * (next_greater[i] - i)

	2.	As Minimum:
	    •	The number of subarrays where nums[i] is the minimum is:
        (distance to previous greater element) * (distance to next greater element)
	    •	Formula:
        (min contribution) = nums[i] * (i - prev_smaller[i]) * (next_smaller[i] - i)


2. Use Monotonic Stacks
	•	Use stacks to compute:
	•	prev_smaller and next_smaller for minimum contributions.
	•	prev_greater and next_greater for maximum contributions.

3. Calculate Total Contribution
	•	For each element nums[i], compute:
        Contribution = max contribution - min contribution
	•	Sum these contributions for all elements.
'''

from collections import deque
from typing import List
class Solution:
    '''Solution Class'''

    def get_next_and_prev_smaller_greater(self, arr) -> int:
        '''Helper function'''
        n = len(arr)
        next_smaller = [n for x in arr]
        prev_smaller = [-1 for x in arr]

        next_greater = [n for x in arr]
        prev_greater = [-1 for x in arr]
        stack  = deque()

        # Next and previous smaller
        for idx, num in enumerate(arr):
            while len(stack) > 0 and arr[stack[-1]] > num:
                next_smaller[stack.pop()] = idx
                # This while loop will end:
                    # 1. When no elements in the stack
                    # 2. Element on top of the stack is < arr[idx]
                        # we can update prev_smaller of curr idx to stack[-1]
            prev_smaller[idx] = stack[-1] if len(stack) else -1
            stack.append(idx)

        # Calculate next greater and previous greater
        stack = deque()
        for idx, num in enumerate(arr):

            while len(stack) and arr[stack[-1]] < num:
                next_greater[stack.pop()] = idx
            prev_greater[idx] = stack[-1] if len(stack) > 0 else -1
            stack.append(idx)

        return next_smaller, prev_smaller, next_greater, prev_greater

    def sub_array_ranges(self, nums: List[int]) -> int:
        '''Main Function'''   
        n = len(nums)
        if n == 0:
            return 0

        result = self.get_next_and_prev_smaller_greater(nums)
        next_smaller, prev_smaller, next_greater, prev_greater = result
        tot_sum = 0
        for i, num in enumerate(nums):

            max_contribution = num * ((i - prev_greater[i]) * (next_greater[i] - i))
            min_contribution = num * ((i - prev_smaller[i]) * (next_smaller[i] - i))
            tot_sum += max_contribution - min_contribution
        return tot_sum
