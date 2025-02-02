"""
Depth-First Search (DFS) Path Finding Visualization

Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V) for visited set and recursion stack
"""

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
    
    def visualize_graph(self):
        """Returns a string representation of the graph"""
        result = "Graph Structure:\n"
        for node in sorted(self.graph.keys()):
            result += f"{node} → {' → '.join(map(str, self.graph[node]))}\n"
        return result
    
    def dfs_path_exists(self, start: int, end: int) -> bool:
        visited = set()
        path = []  # To track the current path
        
        def dfs(node, depth=0):
            # Add visualization of current step
            indent = "  " * depth
            print(f"{indent}Visiting node: {node}")
            
            if node == end:
                path.append(node)
                print(f"{indent}Found end node!")
                return True
            
            visited.add(node)
            path.append(node)
            print(f"{indent}Current path: {' → '.join(map(str, path))}")
            
            for neighbor in self.graph.get(node, []):
                print(f"{indent}Checking neighbor: {neighbor}")
                if neighbor not in visited:
                    if dfs(neighbor, depth + 1):
                        return True
            
            path.pop()
            print(f"{indent}Backtracking from node {node}")
            return False
        
        return dfs(start)

def visualize_test_case(case, index):
    """Visualizes a single test case"""
    print(f"\nTest Case {index}:")
    print("=" * 50)
    
    # Create and populate graph
    g = Graph()
    for u, v in case['edges']:
        g.add_edge(u, v)
    
    # Print graph structure
    print(g.visualize_graph())
    
    # Print test case details
    print(f"Finding path from {case['start']} to {case['end']}")
    print("\nDFS Path Finding Process:")
    print("-" * 30)
    
    # Run DFS
    result = g.dfs_path_exists(case['start'], case['end'])
    
    # Print result
    print("\nResult:")
    print(f"Path exists: {result}")
    print("=" * 50)

# Enhanced test cases with visual representations
test_cases = [
    {
        'edges': [(0,1), (1,2), (2,3)],
        'start': 0,
        'end': 3,
        'description': """
        Linear Path:
        0 → 1 → 2 → 3
        """
    },
    {
        'edges': [(0,1), (2,3)],
        'start': 0,
        'end': 3,
        'description': """
        Disconnected Components:
        0 → 1    2 → 3
        """
    },
    {
        'edges': [(0,1), (1,2), (2,0), (2,3)],
        'start': 0,
        'end': 3,
        'description': """
        Cyclic Graph:
        0 → 1
        ↑   ↓
        2 → 3
        """
    }
]

def run_tests():
    for i, case in enumerate(test_cases, 1):
        print("\nTest Case Description:")
        print(case['description'])
        visualize_test_case(case, i)

if __name__ == "__main__":
    run_tests()