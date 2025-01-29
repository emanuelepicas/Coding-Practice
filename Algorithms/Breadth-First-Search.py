"""
Question: Given a binary tree, return the level-order traversal of its nodes' values.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Test Cases
def create_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

test_cases = [
    [3,9,20,None,None,15,7],  # Normal binary tree
    [1],                      # Single node
    [],                       # Empty tree
    [1,2,3,4,5]              # Complete binary tree
]

for values in test_cases:
    root = create_tree(values)
    result = level_order_traversal(root)
    print(f"Input tree values: {values}")
    print(f"Level order traversal: {result}")
    print("-" * 40)