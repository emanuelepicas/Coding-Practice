"""
Question: Implement DFS to find if a path exists between two nodes in a graph.
Return True if path exists, False otherwise.
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
        
    def dfs_path_exists(self, start: int, end: int) -> bool:
        visited = set()
        
        def dfs(node):
            if node == end:
                return True
            
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(start)

# Test Cases
test_cases = [
    # Test Case 1: Simple path
    {
        'edges': [(0,1), (1,2), (2,3)],
        'start': 0,
        'end': 3
    },
    # Test Case 2: No path
    {
        'edges': [(0,1), (2,3)],
        'start': 0,
        'end': 3
    },
    # Test Case 3: Cyclic graph
    {
        'edges': [(0,1), (1,2), (2,0), (2,3)],
        'start': 0,
        'end': 3
    }
]

for case in test_cases:
    g = Graph()
    for u, v in case['edges']:
        g.add_edge(u, v)
    
    result = g.dfs_path_exists(case['start'], case['end'])
    print(f"Edges: {case['edges']}")
    print(f"Path from {case['start']} to {case['end']} exists: {result}")
    print("-" * 40)