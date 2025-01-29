class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def display(self):
        return str(self.graph)

# Visual Example:
"""
Initial: {}
After adding vertices A, B, C:
{
    'A': [],
    'B': [],
    'C': []
}
After adding edges (A-B, B-C):
{
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}
"""

# Usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
print(graph.display())