class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Check if there exists a root-to-leaf path with given sum
        Time: O(n)
        Space: O(h)
        """
        def dfs(node, current_sum):
            if not node:
                return False
            
            current_sum += node.val
            
            # If leaf node, check sum
            if not node.left and not node.right:
                return current_sum == targetSum
            
            # Check both subtrees
            return (dfs(node.left, current_sum) or 
                   dfs(node.right, current_sum))
            
        return dfs(root, 0)