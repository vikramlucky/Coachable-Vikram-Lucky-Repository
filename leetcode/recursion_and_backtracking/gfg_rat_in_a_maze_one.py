'''
Consider a rat placed at position (0, 0) in an n x n square matrix mat. 
The rat's goal is to reach the destination at position (n-1, n-1). 
The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

The matrix contains only two possible values:

0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Note: In a path, no cell can be visited more than one time. 
If the source cell is 0, the rat cannot move to any other cell. 
In case of no path, return an empty list.+

The task is to find all possible paths the rat can take to reach the destination, 
starting from (0, 0) and ending at (n-1, n-1), 
under the condition that the rat cannot revisit any cell along the same path.
Furthermore, the rat can only move to adjacent cells that are within the 
bounds of the matrix and not blocked.

EXAMPLE:

Input: mat[][] = [[1, 0, 0, 0], 
                  [1, 1, 0, 1], 
                  [1, 1, 0, 0], 
                  [0, 1, 1, 1]]

Output: ["DDRDRR", "DRDDRR"]
Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths 
- DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.

Time: (4 ^ (n * m)) i.e from each cell there are 4 possible direction we can explore
Space: (N * M)
'''

from typing import List

class Solution:
    '''Solution Class'''

    def find_path(self, mat):
        '''main function'''
        if not mat or not mat[0]:
            return []

        if mat[0][0] == 0 or mat[-1][-1] == 0:
            return []

        ans = []
        self.backtrack((0, 0), mat, "", ans)
        return sorted(ans)

    def backtrack(self, pos: tuple, grid: List[List[int]], path: str, ans: List[str]):
        '''Helper Funtion'''
        x, y = pos
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            ans.append(path)
            return

        original_value = grid[x][y]
        grid[x][y] = -1

        for dx, dy, d in ((-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')):
            new_x = dx + x
            new_y = dy + y

            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                self.backtrack((new_x, new_y), grid, path + d, ans)

        grid[x][y] = original_value
