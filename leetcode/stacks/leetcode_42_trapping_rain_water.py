'''
Leetcode 42 Trapping Rain Water

Problem Statement:
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is 
represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Observation:
For each index i, the maximum water that can be trapped is determined by the 
heights of the tallest bars to its left and right:

Water at i = min(max_left[i], max_right[i]) - heights[i]

Where:
	•	max_left[i]: Maximum height of bars to the left of i.
	•	max_right[i]: Maximum height of bars to the right of i.

Approach 1: Precompute max_left and max_right 
	1.	Precompute max_left:
	    •	Traverse the heights array from left to right and compute the maximum height seen so far at 
        each index.
	2.	Precompute max_right:
	    •	Traverse the heights array from right to left and compute the maximum height seen so far at 
        each index.
	3.	Iterate through the array:
	    •	For each index i, calculate the trapped water as:

    Water at i = min(max_left[i], max_right[i]) - heights[i]

	•	Add the result to a total_water variable.

Time: O(n), Space: O(n)

Approach 2: Two Pointers

This approach optimizes space usage by avoiding the explicit construction 
of max_left and max_right arrays.

Steps
	1.	Use two pointers:
	    •	left starting at index 0 and right at index n-1.
	2.	Use two variables:
	    •	max_left to track the maximum height seen so far from the left.
	    •	max_right to track the maximum height seen so far from the right.
	3.	While left <= right:
	    •	If height[left] <= height[right]:
	        •   If height[left] >= max_left, update max_left to height[left].
	        •	Otherwise, add max_left - height[left] to total_water.
	        •	Increment the left pointer.

	    •	Otherwise:
	        •	If height[right] >= max_right, update max_right to height[right].
	        •	Otherwise, add max_right - height[right] to total_water.
	        •	Decrement the right pointer.
	4.	Return total_water.

Complexity
•	Time: O(n) — Single pass through the array using the two pointers.
•	Space: O(1) — No additional arrays used.
'''

from typing import List
class Solution:
    '''Solution Class'''

    # Optimized solution O(1) Space
    def trap(self, height: List[int]) -> int:
        '''Main function'''

        max_water = 0
        n = len(height)
        if n == 0:
            return max_water

        left, max_left = 0, 0
        right, max_right = n - 1, 0

        while left <= right:

            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    max_water += max_left - height[left]
                left += 1

            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    max_water += max_right - height[right]

                right -= 1

        return max_water




    def get_max_height_left_right(self, arr: List[int]) -> List[int]:
        '''Helper function for Solution using O(n) space'''

        n = len(arr)
        if n == 0:
            return ([],[])

        left_max = [0 for x in arr]
        right_max = [0 for x in arr]

        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(arr[i], left_max[i - 1])

        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])

        return (left_max, right_max)

    def trap_1(self, height: List[int]) -> int:
        '''Not spaced optimized solution'''

        n = len(height)
        if n == 0:
            return 0

        left_max, right_max = self.get_max_height_left_right(height)
        total_rain = 0

        for idx, h in enumerate(height):
            min_height = min(left_max[idx], right_max[idx])
            total_rain += min_height - h

        return total_rain
