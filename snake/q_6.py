import networkx as nx

G = nx.Graph()
edges = [
    ("A", "B", 3), ("A", "E", 2),
    ("B", "C", 1), ("B", "E", 2), ("B", "F", 4),
    ("C", "D", 3), ("C", "F", 2), ("C", "G", 2),
    ("D", "G", 1), ("D", "H", 4),
    ("E", "F", 1),
    ("F", "G", 3),
    ("G", "H", 2),
]

G.add_weighted_edges_from(edges)

# Use Kirchhoff's theorem (Matrix-Tree)
spanning_trees = nx.number_of_spanning_trees(G)
print("Number of spanning trees:", spanning_trees)
