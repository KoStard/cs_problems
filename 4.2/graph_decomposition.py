# Problem N3
# We need to find the components in the graph. Currently thinking about doing DFS, marking all notes 
# that are connected with some other node, repeat on the nodes that are not connected. Based on these marks
# we'll be able to generate the components.

# For graph representation thinking about keeping the set of vertices and map of vertices for edges

from collections import defaultdict

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges_for_representation = edges
        self.edge_map = defaultdict(set)

        for edge in edges:
            edge_iterator = iter(edge)
            self.add_edge(next(edge_iterator), next(edge_iterator))

    def add_edge(self, v1, v2):
        self.edge_map[v1].add(v2)
        self.edge_map[v2].add(v1)

    def __str__(self) -> str:
        return "Graph with vertices: {}\nAnd edges: {}".format(self.vertices, self.edges_for_representation)


class GraphDecomposer:
    # will decompose graphs into components
    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        self.marks = {}

    def decompose(self):
        for v in self.graph.vertices:
            if v not in self.marks:
                self.dfs_marking(v, v)
        vertex_groups = defaultdict(set)
        for v, mark in self.marks.items():
            vertex_groups[mark].add(v)

        component_graphs = []

        for component_vertices in vertex_groups.values():
            edges = set()
            for v in component_vertices:
                for v2 in self.graph.edge_map[v]:
                    edges.add(frozenset((v, v2)))
            component_graph = Graph(component_vertices, edges)
            component_graphs.append(component_graph)
        return component_graphs

    def dfs_marking(self, v, mark):
        self.marks[v] = mark
        for v2 in self.graph.edge_map[v]:
            if v2 not in self.marks:
                self.dfs_marking(v2, mark)



graph = Graph(list(range(10)), [
    [0, 1],
    [2, 3],
    [3, 4],
    [4, 5],
    [6, 7],
    [7, 8],
    [8, 9]
])

components = GraphDecomposer(graph).decompose()
print(*components, sep='\n')