"""
Leetcode 426:

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and 
successor pointers in a doubly-linked list. For a circular doubly linked list, 
the predecessor of the first element is the last element, 
and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, 
the left pointer of the tree node should point to its predecessor, 
and the right pointer should point to its successor. 
You should return the pointer to the smallest element of the linked list.
"""

from typing import Optional


class Node:
    """A Node definition"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """A solution class"""

    def __init__(self, tail = Node(-1)):
        self.tail = tail

    def tree_to_dll(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """Main function take root of BST and return head node of dll"""

        if not root:
            return root

        dummy = self.tail
        self.convert_tree_dll(root)
        dummy.right.left, self.tail.right = self.tail, dummy.right
        return dummy.right

    def convert_tree_dll(self, node):
        """Helper function: Traverse tree in Inorder and adjust pointers"""

        if node is None:
            return

        # Inorder Traversal: Go left
        self.convert_tree_dll(node.left)

        # Adjust pointers:
        node.left = self.tail
        self.tail.right = node
        self.tail = self.tail.right

        # Go Right
        self.convert_tree_dll(node.right)
