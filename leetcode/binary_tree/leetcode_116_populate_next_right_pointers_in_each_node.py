""" 
Leetcode 116:
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""
from collections import deque

class Node:
    """A Node class for tree nodes"""
    def __init__(self, val =  0, left = None, right = None, next_right = None):
        self.val = val
        self.left = left
        self.right = right
        self.next_right = next_right

class Solution:
    """A solution class."""
    def connect(self, root: Node) -> Node:
        """
        A connect functio take Node as a input, and return same node
        With each node updated with next_right pointers.
        """
        if not root:
            return root

        q = deque()
        q.append(root)

        while len(q) > 0:

            level_size = len(q)
            prev = None

            for _ in range(level_size):
                curr_node = q.popleft()
                curr_node.next = prev

                if curr_node.right:
                    q.append(curr_node.right)
                if curr_node.left:
                    q.append(curr_node.left)   
                prev = curr_node

        return root
