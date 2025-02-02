class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Preorder traversal: Root -> Left -> Right
        Time: O(n)
        Space: O(h)
        """
        def dfs(node, result):
            if not node:
                return
                
            result.append(node.val)    # Process current node
            dfs(node.left, result)     # Process left subtree
            dfs(node.right, result)    # Process right subtree
            
        result = []
        dfs(root, result)
        return result
