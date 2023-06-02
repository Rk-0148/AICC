from queue import PriorityQueue

# Graph class to represent the graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        
    # Function to add an edge to the graph
    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight
        
    # Function to find the minimum spanning tree
    def prim_mst(self):
        # Priority queue to store vertices and their key values
        pq = PriorityQueue()
        
        # List to store the parent of vertices
        parent = [None] * self.V
        
        # List to store the key values of vertices
        key = [float('inf')] * self.V
        
        # List to store if a vertex is included in MST
        mst_set = [False] * self.V
        
        # Start with the first vertex
        start_vertex = 0
        key[start_vertex] = 0
        pq.put((0, start_vertex))
        
        while not pq.empty():
            # Extract the minimum key vertex from the priority queue
            u = pq.get()[1]
            
            # Include the extracted vertex in MST
            mst_set[u] = True
            
            # Update the key values and parent of the adjacent vertices of the extracted vertex
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    pq.put((key[v], v))
                    
        # Print the minimum spanning tree
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

# Example usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim_mst()
