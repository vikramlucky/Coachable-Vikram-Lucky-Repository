"""
Geeks for Geeks: 
https://www.geeksforgeeks.org/problems/number-of-turns-in-binary-tree/1

Given a binary tree and data value of two of its nodes. 
Find the number of turns needed to reach from one node to another in 
the given binary tree.

Example 1:
Input:      
Tree = 
           1
        /    \\
       2       3
     /  \\     /  \\
    4    5   6    7                        
   /        / \\                        
  8        9   10   
first node = 5
second node = 10
Output: 4
Explanation: 
Turns will be at 2, 1, 3, 6.

Example 2:
Input:      
Tree = 
           1
        /    \\
       2        3
     / \\      / \\
    4    5    6    7                        
   /         / \\                        
  8         9   10   
first node = 1
second node = 4  
Output: -1
Explanation: No turn is required since 
they are in a straight line.

Example 3 Input:

        7
       / \\
      5   10

first node = 5
second node = 10  
Output: 1

Example 4 Input:
        
        5
         \\
          7
           \\
             10

first_node = 5
second_node = 10            
OUTPUT: 0 # No turn required
"""
class Solution:
    """A solution class"""

    def __init__(self):
        self.total_turns = 0

    def find_lca(self, root, first, second):
        """Find the lowest common ancestor of two nodes."""
        if not root:
            return None
        if root.data in (first, second):
            return root

        left = self.find_lca(root.left, first, second)
        right = self.find_lca(root.right, first, second)

        if left and right:
            return root

        return left if left else right

    def count_turns(self, root, target, direction):
        """Count the number of turns from root to target node."""
        if not root:
            return False

        if root.data == target:
            return True

        # Check left subtree
        left = self.count_turns(root.left, target, 'LEFT')
        if left:
            if direction == 'RIGHT':  # Increment turns if direction changes
                self.total_turns += 1
            return True

        # Check right subtree
        right = self.count_turns(root.right, target, 'RIGHT')
        if right:
            if direction == 'LEFT':  # Increment turns if direction changes
                self.total_turns += 1
            return True

        return False

    def number_of_turns(self, root, first, second):
        """Return the number of turns required to go from first node to second node."""
        if not root:
            return -1

        if first == second:
            return 0

        # Find LCA of the two nodes
        lca = self.find_lca(root, first, second)
        if not lca:
            return -1

        # Initialize turn counters
        turns_from_first = 0
        turns_from_second = 0

        # Count turns from LCA to the first node
        self.count_turns(lca, first, None)
        turns_from_first = self.total_turns

        # Count turns from LCA to the second node
        self.total_turns = 0  # Reset for independent path
        self.count_turns(lca, second, None)
        turns_from_second = self.total_turns

        # If the nodes are on different subtrees, add 1 turn at the LCA
        if lca.data not in (first, second):
            return turns_from_first + turns_from_second + 1

        # If one of the nodes is the LCA, just return the turns to the other node
        return turns_from_first + turns_from_second
