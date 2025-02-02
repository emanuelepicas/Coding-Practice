from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Level order traversal of binary tree
        Time: O(n) where n is number of nodes
        Space: O(w) where w is maximum width of tree
        """
        if not root:
            return []
            
        result = []
        queue = deque([root])
        print(queue)
        
        while queue:
            level_size = len(queue)
            print(f"current level size {level_size}")
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                print(f"Current node {node}\n")
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(current_level)
            
        return result

