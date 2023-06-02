from collections import deque

# Graph class to represent an undirected graph
class Graph:
    def __init__(self):
        self.graph = {}

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    # Function to perform BFS traversal
    def bfs(self, start):
        visited = set()  # Set to keep track of visited nodes
        queue = deque()  # Queue for BFS traversal

        visited.add(start)
        queue.append(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Testing the algorithm
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Breadth First Traversal (starting from vertex 4):")
g.bfs(2)
