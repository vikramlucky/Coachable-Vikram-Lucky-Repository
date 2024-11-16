"""99. Recover Binary Search Tree.
This module contains the implementation of a solution to recover a binary
search tree where two nodes have been swapped.
"""

# Definition for a binary tree node.
class TreeNode:
    """
    A TreeNode class.

    Attributes:
    ----------
    val : int
        The nodes value
    left : TreeNode
        The left child of the node
    right : TreeNode
        The right child of the node
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    A solution class to recover a BST.

    Attributes:
    ----------
    prev : TreeNode
        The previous node in in-order traversal.
    first : TreeNode
        The first misplaced node.
    second : TreeNode
        The second misplaced node.

    Methods:
    -------
    recover_tree(root: TreeNode) -> TreeNode:
        Main function to identify and swap misplaced nodes.
    
    find_swapped_nodes(root: TreeNode) -> None:
       A Helper function to identify swapped nodes during in-order traversal.
    """

    def __init__(self, prev = None, first = None, second = None):
        self.prev = prev
        self.first = first
        self.second = second

    def recover_tree(self, root: TreeNode) -> None:
        """
        Problem Statement: Two nodes in bst have been swapped.
        Approach:
            - Since the property of bst is given root all the nodes to the left
              should be smaller and all the nodes to the right should be greater.
            - So first step would be to identify swapped nodes: 
                - Traverse BST in inorder, keep tracking of previous node 
              if at any point val of previous is greater than curr / root node, 
              then will store nodes in first and second respectively. 
            - Once we have identified the swapped nodes, Then will simply swap 
            there value and return the root node.
        
        Time: O(n) n = # of nodes in the bst
        Space: O(h) h = height of bst
        """

        self.find_swapped_nodes(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root

    def find_swapped_nodes(self, root: TreeNode) -> None:
        """
        Identifies the two swapped nodes in BST.

        Parameters
        ----------
        root: TreeNode
            The root node of the BST.
        """

        if not root:
            return
        
        # Inorder traversal: Go left -> property check -> go right
        self.find_swapped_nodes(root.left)

        # check the current node against the previous node
        if self.prev and self.prev.val > root.val:

            if not self.first:
                self.first = self.prev
            self.second = root

        self.prev = root
        self.find_swapped_nodes(root.right)