class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(val)
                return
            if not node.right:
                node.right = TreeNode(val)
                return
            queue.append(node.left)
            queue.append(node.right)
    
    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)
        return result

# Visual Example:
"""
After insert(1):
    1

After insert(2):
    1
   /
  2

After insert(3):
    1
   / \
  2   3
"""

# Usage:
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
print(tree.inorder_traversal(tree.root))  # [2, 1, 3]