class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find minimum depth of binary tree using BFS
        Time: O(n)
        Space: O(w)
        """
        if not root:
            return 0
            
        queue = deque([(root, 1)])  # (node, depth) pairs
        
        while queue:
            node, depth = queue.popleft()
            
            # If leaf node, return its depth
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))