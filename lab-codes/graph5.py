import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge(1,2,weight=0.5)
G.add_edge(1,3,weight=0.7)

G.add_node("a")

G.add_nodes_from(["b","c"])

nx.draw(G, with_labels=True)



print(G.nodes())
print(G.edges())



plt.show()
