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

    # Recursive function for DFS traversal
    def dfs_util(self, v, visited):
        # Mark the current node as visited
        visited.add(v)
        print(v, end=' ')

        # Recur for all the adjacent vertices
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    # Function to perform DFS traversal
    def dfs(self, start):
        visited = set()  # Set to keep track of visited nodes
        self.dfs_util(start, visited)

# Testing the algorithm
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Depth First Traversal (starting from vertex 4):")
g.dfs(4)
