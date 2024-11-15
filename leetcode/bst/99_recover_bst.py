"""99. Recover Binary Search Tree"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self, prev = None, first = None, second = None):
        self.prev = prev
        self.first = first
        self.second = second

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Problem Statement: Two nodes in bst have been swapped.
        Approach:
            - Since the property of bst is given root all the nodes to the left should be smaller and all the nodes to the right should be greater.
            - So first step would be to identify swapped nodes: Traverse BST in inorder, keep tracking of previous node 
              if at any point val of previous is greater than curr / root node, then will store nodes in first and second respectively. 
            - Once we have identified the swapped nodes, Then will simply swap there value and return the root node.
        
        Time: O(n) n = # of nodes in the bst
        Space: O(h) h = height of bst

        """
        self.find_swapped_nodes(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root

    def find_swapped_nodes(self, root):

        if not root:
            return
        
        # Inorder traversal: Go left -> do your stuff -> go right
        self.find_swapped_nodes(root.left)

        # Do your stuff
        if self.prev and self.prev.val > root.val:

            if not self.first:
                self.first = self.prev
            self.second = root
        
        self.prev = root
        self.find_swapped_nodes(root.right)

        

        