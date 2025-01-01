'''
79. Word Search
https://leetcode.com/problems/word-search/description/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Approach:

Solved using backtrack:
Space: O(L)
Time: O(N * 3 ^ L) 
# N = number of total cells in the board
# 3 ^ L => 3 possibile direction, L => longest length of the string

'''

from typing import List
class Solution:
    '''Solution class'''
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''Main function'''

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and self.found(0, word, board, r, c):
                    return True
        return False

    def found(self, idx: int, word: str, board: List[List[str]], r: int, c: int):
        '''Helper backtrack function'''

        #Base case
        if idx + 1 >= len(word):
            return True

        curr_ch = board[r][c]
        board[r][c] = '*'

        for ix, iy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_r = r + ix
            new_c = c + iy

            if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]):

                if word[idx + 1] == board[new_r][new_c]:
                    if self.found(idx + 1, word, board, new_r, new_c):
                        board[r][c] = curr_ch
                        return True
        board[r][c] = curr_ch
        return False
