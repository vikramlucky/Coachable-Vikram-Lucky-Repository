"""Leetcode_735_Asteroid_Collision

Problem Statement:

We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves 
at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Approach:

Will solve using stack:

    Collision possibilities: 
        1. When previous element (Top of stack) is > 0 and current (incoming asteroid) < 0:
            -> If val of previous asteroid is less than abs val of incoming asteroid.
                -> previous gets destroyed
            -> If val of previous asteroid is == abs val of incoming asteroid 
                -> Both gets destryed
            -> If val of previous asteroid is > abs val of incoming asteroid
                -> incoming asteroid gets destroyed
        
            Will repeat above steps as long as we have elements in the stack and top element is > 0,
            and current asteroid is not destroyed
        2. If current asteroid survives add it to the stack

"""

from collections import deque
from typing import List
class Solution:
    '''Solution class'''
    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        '''Main function'''

        stack = deque()

        for asteroid in asteroids:

            # Possible collision
            while len(stack) > 0 and stack[-1] > 0 > asteroid:

                if stack[-1] < abs(asteroid):
                    stack.pop()

                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    asteroid = 0

                else:
                    asteroid = 0
            # If asteroid survives
            if asteroid:
                stack.append(asteroid)

        return stack
