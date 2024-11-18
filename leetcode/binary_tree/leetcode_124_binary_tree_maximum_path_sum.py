"""124. Binary tree maximum path sum
This module contains the implementation of a solution to Binary tree maximum path sum
"""

# Definition for a binary tree node.
class TreeNode1:
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
    A solution class to get maximum path.

    Attributes:
    ----------
    maximum_path_sum : int
        maximum sum seem so far
   

    Methods:
    -------
    max_path_sum(root: TreeNode) -> int:
        Main function, calls helper function and returns the result.
    
    calculate_path_sum(root: TreeNode) -> int:
       A Helper function to calculate and update maximum path sum
    """

    def __init__(self, maximum_path_sum = float("-inf")):
        self.maximum_path_sum = maximum_path_sum

    def calculate_path_sum(self, node: TreeNode1):
        """
        A helper function:
        Calculates maximum path sum
        """

        if not node:
            return 0
        left = max(self.calculate_path_sum(node.left), 0)
        right = max(self.calculate_path_sum(node.right), 0)

        curr_sum = left + right + node.val
        self.maximum_path_sum = max(self.maximum_path_sum, curr_sum)

        return max(left, right) + node.val

    def max_path_sum(self, root: TreeNode1) -> int:
        """
        Main Function: 
        -Calls helper function and returns the result
        """

        self.calculate_path_sum(root)
        return self.maximum_path_sum
