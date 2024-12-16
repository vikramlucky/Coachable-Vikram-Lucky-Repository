"""https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/
Given a binary tree in which each node element contains a number.
Find the maximum possible sum from one leaf node to another.
"""

class TreeNode:
    """
    A TreeNode class
    """

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    """
    A solution class to get maximum path between two leaf nodes.

    Attributes:
    ----------
    max_sum : int

    Methods:
    -------
    max_path_sum_leaves(root: TreeNode) -> int:
        Main function, calls helper function and calculates the max sum
    
    helper(root: TreeNode):
       A Helper function to calculate and update maximum path sum
    """

    def __init__(self):
        self.max_sum = float('-inf')  # Initialize the global maximum

    def max_path_sum_leaves(self, root: TreeNode) -> None:
        """
        This function takes a TreeNode, and calculate the max
        path sum between two nodes.
        """
        if not root:
            return 0

        # Helper function to calculate the path sum
        def helper(node):
            if not node:
                return 0

            # Recursively calculate sums for left and right subtrees
            left_sum = helper(node.left)
            right_sum = helper(node.right)

            # If the node is a leaf, return its value
            if not node.left and not node.right:
                return node.val

            # If both children exist, update the global maximum
            if node.left and node.right:
                self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)
                # Return the maximum path sum going up the tree
                return max(left_sum, right_sum) + node.val

            # If only one child exists, return the sum for that child
            return (left_sum if node.left else right_sum) + node.val

        # Trigger the recursion
        helper(root)

        # Return the maximum path sum found
        return self.max_sum if self.max_sum != float('-inf') else 0
