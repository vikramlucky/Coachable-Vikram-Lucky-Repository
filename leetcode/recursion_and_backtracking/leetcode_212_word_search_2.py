'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example: 
Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]],

       words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

'''

from typing import List
class TrieNode:
    '''TrieNode class'''
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    '''Solution Class'''
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''Main solution function'''

        root = TrieNode()

        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word

        result = set()
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch in root.children:
                    self.backtrack((i, j), result, board, root)
        return list(result)

    def backtrack(self, pos: tuple, res: set, board: List[List[str]], root: TrieNode):
        '''Helper backtracking function'''
        x, y = pos
        curr_ch = board[x][y]
        curr_node = root.children[curr_ch]

        if curr_node.word:
            res.add(curr_node.word)

        board[x][y] = '*'

        for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            new_x, new_y = dx + x, dy + y

            is_bound = 0 <= new_x < len(board) and 0 <= new_y < len(board[0])
            if is_bound and board[new_x][new_y] in curr_node.children:
                self.backtrack((new_x, new_y), res, board, curr_node)

        board[x][y] = curr_ch

        if not curr_node.children:
            del root.children[curr_ch]
