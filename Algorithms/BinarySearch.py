"""
Binary Tree Level Order Traversal

Time Complexity: O(n) where n is the number of nodes
- We visit each node exactly once

Space Complexity: O(w) where w is the maximum width of the tree
- In worst case (complete binary tree), the queue can contain up to n/2 nodes
  (all leaf nodes at the last level)

Example Tree Structure:
     3
   /   \
  9    20
      /  \
     15   7

Level Order Output: [[3], [9,20], [15,7]]
"""

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Performs level-order traversal of a binary tree using BFS.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of lists containing values at each level
        
    Time Complexity: O(n)
    Space Complexity: O(w) where w is the maximum width of the tree
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)  # Number of nodes at current level
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

def create_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Creates a binary tree from a list of values.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Create left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Create right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def print_tree(root: Optional[TreeNode]) -> None:
    """
    Prints a visual representation of the binary tree.
    """
    if not root:
        print("Empty Tree")
        return
    
    def get_height(node):
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))
    
    def print_level(node, level, space):
        if not node:
            return
        if level == 1:
            print(" " * space + str(node.val), end="")
        elif level > 1:
            print_level(node.left, level - 1, space)
            print_level(node.right, level - 1, space)
    
    height = get_height(root)
    for i in range(1, height + 1):
        print_level(root, i, height - i)
        print()

# Test Cases with detailed examples
test_cases = [
    # Test Case 1: Normal binary tree
    {
        'values': [3,9,20,None,None,15,7],
        'description': """
        Normal binary tree:
             3
           /   \\
          9    20
              /  \\
             15   7
        """
    },
    # Test Case 2: Complete binary tree
    {
        'values': [1,2,3,4,5,6,7],
        'description': """
        Complete binary tree:
             1
           /   \\
          2     3
         / \\   / \\
        4   5 6   7
        """
    }
]

def run_tests():
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(test_case['description'])
        
        values = test_case['values']
        root = create_tree(values)
        
        print("\nTree Visualization:")
        print_tree(root)
        
        result = level_order_traversal(root)
        print(f"\nInput values: {values}")
        print(f"Level order traversal: {result}")
        
        # Print level-by-level explanation
        print("\nLevel-by-level breakdown:")
        for level_num, level_values in enumerate(result):
            print(f"Level {level_num}: {level_values}")
        
        print("-" * 60)

if __name__ == "__main__":
    run_tests()