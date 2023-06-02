# Helper class to represent a graph edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

# Helper class to represent a disjoint set
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

# Main Kruskal's algorithm implementation
def kruskal(graph):
    edges = []
    for src in graph:
        for dest, weight in graph[src]:
            edges.append(Edge(src, dest, weight))

    # Sort edges in ascending order based on weight
    edges.sort(key=lambda x: x.weight)

    mst = []
    disjoint_set = DisjointSet(graph.keys())

    for edge in edges:
        src_root = disjoint_set.find(edge.src)
        dest_root = disjoint_set.find(edge.dest)

        if src_root != dest_root:
            mst.append(edge)
            disjoint_set.union(src_root, dest_root)

    return mst

# Example usage
graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 3), ('D', 3)],
    'C': [('B', 3), ('D', 1)],
    'D': [('A', 5), ('B', 3), ('C', 1)]
}

minimum_spanning_tree = kruskal(graph)

# Print the edges of the minimum spanning tree
for edge in minimum_spanning_tree:
    print(f'{edge.src} -- {edge.dest}: {edge.weight}')
