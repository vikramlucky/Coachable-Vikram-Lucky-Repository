"""
Leetcode 863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.
"""
from collections import deque, defaultdict
from typing import List

class TreeNode:
    """A Binary TreeNode class"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """A solution class."""

    def get_parent_child_map(self, node: TreeNode) -> defaultdict:
        """Function get a tree node and return a dictionary of parent child mapping."""
        q = deque()
        q.append(node)
        parent_child_set = defaultdict(TreeNode)

        while len(q) > 0:
            curr_node = q.popleft()

            if curr_node.left:
                q.append(curr_node.left)
                parent_child_set[curr_node.left.val] = curr_node
            if curr_node.right:
                q.append(curr_node.right)
                parent_child_set[curr_node.right.val] = curr_node

        return parent_child_set

    def distance_k(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """Function distance k: return all the nodes distance k from target node"""
        if not root or not target:
            return []

        parent_child_map = self.get_parent_child_map(root)
        q = deque()
        seen = set()

        q.append(target)
        seen.add(target.val)

        while len(q) > 0:

            if k == 0:
                break
            k -= 1
            level_size = len(q)

            for _ in range(level_size):

                curr_node = q.popleft()

                #Adding left child
                if curr_node.left and curr_node.left.val not in seen:
                    seen.add(curr_node.left.val)
                    q.append(curr_node.left)

                # Adding right child
                if curr_node.right and curr_node.right.val not in seen:
                    seen.add(curr_node.right.val)
                    q.append(curr_node.right)

                # Adding parent
                is_in_map = curr_node.val in parent_child_map
                not_in_seen = parent_child_map[curr_node.val].val not in seen

                if is_in_map and not_in_seen:
                    q.append(parent_child_map[curr_node.val])
                    seen.add(parent_child_map[curr_node.val].val)

        return [node.val for node in q]
