"""
Geeksforgeeks: https://www.geeksforgeeks.org/problems/k-sum-paths/1
Given a binary tree and an integer k, 
the task is to count the number of paths in the tree such that the 
sum of the nodes in each path equals k. 
A path can start from any node and end at any node and must be downward only.
"""

from collections import defaultdict

class Node:
    """A Treenode class definition"""
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    """A Solution class."""

    def __init__(self, count = 0):
        self.count = count

    def sum_k(self,root,k):
        """Main function takes treenode root and k: return paht counts"""
        prefix_seen = defaultdict(int)
        prefix_seen[0] = 1
        self.helper(root, k, prefix_seen, 0)

        return self.count

    def helper(self, root, k, prefix_sum, curr_sum) -> None:
        """A helper function calculate # of paths equal k"""

        if not root:
            return 0

        curr_sum += root.data
        if curr_sum - k in prefix_sum:
            self.count += prefix_sum[curr_sum - k]
        prefix_sum[curr_sum] += 1

        self.helper(root.left, k, prefix_sum, curr_sum)
        self.helper(root.right, k, prefix_sum, curr_sum)

        prefix_sum[curr_sum] -= 1
        if prefix_sum[curr_sum] == 0:
            del prefix_sum[curr_sum]

        return None
