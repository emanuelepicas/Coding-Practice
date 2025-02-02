class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Find all root-to-leaf paths using pre-order traversal
        
        Time Complexity: O(N) where N is number of nodes
        Space Complexity: O(H) where H is height of tree
        """
        if not root:
            return []
        
        paths = []
        
        def preorder(node: TreeNode, current_path: str):
            # Add current node to path
            if not current_path:
                current_path = str(node.val)
            else:
                current_path += "->" + str(node.val)
            
            # If leaf node, add path to results
            if not node.left and not node.right:
                paths.append(current_path)
                return
            
            # Recurse on left and right children
            if node.left:
                preorder(node.left, current_path)
            if node.right:
                preorder(node.right, current_path)
        
        preorder(root, "")
        return paths

def visualize_tree_paths(root: TreeNode):
    """
    Visualize the process of finding all paths
    """
    def print_tree(node: TreeNode, level: int = 0, prefix: str = "Root: "):
        if not node:
            return
        print("  " * level + prefix + str(node.val))
        if node.left:
            print_tree(node.left, level + 1, "L--- ")
        if node.right:
            print_tree(node.right, level + 1, "R--- ")
    
    print("\nTree Structure:")
    print_tree(root)
    
    solution = Solution()
    paths = solution.binaryTreePaths(root)
    
    print("\nPaths Found:")
    for i, path in enumerate(paths, 1):
        print(f"Path {i}: {path}")

def create_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Create binary tree from level-order traversal values"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
test_cases = [
    {
        'values': [1,2,3,None,5],
        'expected': ["1->2->5","1->3"],
        'description': "Example 1 from problem"
    },
    {
        'values': [1],
        'expected': ["1"],
        'description': "Single node tree"
    },
    {
        'values': [1,2,3,4,5],
        'expected': ["1->2->4","1->2->5","1->3"],
        'description': "Complete binary tree"
    },
    {
        'values': [1,None,2],
        'expected': ["1->2"],
        'description': "Right-skewed tree"
    }
]

def run_tests():
    for i, case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {case['description']}")
        print("=" * 50)
        
        # Create tree
        root = create_tree(case['values'])
        
        # Visualize process
        visualize_tree_paths(root)
        
        # Get actual result
        solution = Solution()
        result = solution.binaryTreePaths(root)
        
        # Verify result
        print(f"\nExpected: {case['expected']}")
        print(f"Got: {result}")
        assert sorted(result) == sorted(case['expected']), \
            f"Test case failed! Expected {case['expected']}, got {result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()