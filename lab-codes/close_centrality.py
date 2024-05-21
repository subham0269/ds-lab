import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()

plt.figure(figsize =(15, 15))
nx.draw_networkx(G, with_labels = True)

close_centrality = nx.closeness_centrality(G)

# G is the Karate Social Graph
print(close_centrality)

