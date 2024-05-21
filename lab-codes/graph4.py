import networkx as nx
from matplotlib import pyplot as plt


G = nx.Graph()

# fixing the size of the figure 
plt.figure(figsize =(10, 7)) 

node_color = [G.degree(v) for v in G] 
# node colour is a list of degrees of nodes 

node_size = [0.0005 * nx.get_node_attributes(G, 'population')[v] for v in G] 
# size of node is a list of population of cities 

edge_width = [0.0015 * G[u][v]['weight'] for u, v in G.edges()] 
# width of edge is a list of weight of edges 

nx.draw_networkx(G, node_size = node_size, 
				node_color = node_color, alpha = 0.7, 
				with_labels = True, width = edge_width, 
				edge_color ='.4', cmap = plt.cm.Blues) 

plt.axis('off') 
plt.tight_layout(); 
