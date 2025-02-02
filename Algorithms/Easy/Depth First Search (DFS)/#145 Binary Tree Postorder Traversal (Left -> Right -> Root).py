class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Postorder traversal: Left -> Right -> Root
        Time: O(n)
        Space: O(h)
        """
        def dfs(node, result):
            if not node:
                return
                
            dfs(node.left, result)     # Process left subtree
            dfs(node.right, result)    # Process right subtree
            result.append(node.val)    # Process current node
            
        result = []
        dfs(root, result)
        return result