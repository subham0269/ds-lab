import matplotlib.pyplot as plt
import networkx as nx

import networkx as nx

G = nx.DiGraph()

edges = [(1, 2), (1, 6), (2, 3), (2, 4), (2, 6),
		(3, 4), (3, 5), (4, 8), (4, 9), (6, 7)]

G.add_edges_from(edges)
nx.draw_networkx(G, with_label = True)

print("Total number of nodes: ", int(G.number_of_nodes()))
print("Total number of edges: ", int(G.number_of_edges()))
print("List of all nodes: ", list(G.nodes()))
print("List of all edges: ", list(G.edges(data = True)))
print("Degree for all nodes: ", dict(G.degree()))

							

bet_centrality = nx.betweenness_centrality(G, normalized = True,
											endpoints = False)

# G is the Karate Social Graph, parameters normalized
# and endpoints ensure whether we normalize the value
# and consider the endpoints respectively.
print(bet_centrality)
