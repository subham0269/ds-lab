import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()

plt.figure(figsize =(15, 15))
nx.draw_networkx(G, with_labels = True)


deg_centrality = nx.degree_centrality(G)

# G is the Karate Club Graph
print(deg_centrality)
