class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two trees are identical
        Time: O(min(n1,n2))
        Space: O(min(h1,h2))
        """
        def dfs(node1, node2):
            # Base cases
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            # Check current nodes and recursively check subtrees
            return (node1.val == node2.val and 
                    dfs(node1.left, node2.left) and 
                    dfs(node1.right, node2.right))
            
        return dfs(p, q)