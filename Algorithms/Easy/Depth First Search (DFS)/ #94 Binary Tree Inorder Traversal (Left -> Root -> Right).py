class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Inorder traversal: Left -> Root -> Right
        Time: O(n)
        Space: O(h) where h is height of tree
        """
        def dfs(node, result):
            if not node:
                return
            
            dfs(node.left, result)    # Process left subtree
            result.append(node.val)    # Process current node
            dfs(node.right, result)    # Process right subtree
            
        result = []
        dfs(root, result)
        return result