"""
Leetcode 109: Given the head of a singly linked list 
where elements are sorted in ascending order, convert it to a 
height-balanced
"""
from typing import Optional

class TreeNode:
    """A definition of TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list.
class ListNode:
    """A definition of ListNode class"""
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node

class Solution:
    """A solution class"""
    def list_to_bst(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """This function takes head node linked list and return a root node of BST"""

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        # Create root from middle node
        slow = head
        fast = head
        slow_prev = None

        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        if slow_prev.next:
            slow_prev.next = None

        root_node = TreeNode(slow.val)
        slow_next = slow.next
        slow.next = None

        root_node.left = self.list_to_bst(head)
        root_node.right = self.list_to_bst(slow_next)

        return root_node
