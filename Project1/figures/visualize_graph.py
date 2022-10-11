import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node('a 47', pos=(1,9))
G.add_node('b 31', pos=(3,6))
G.add_node('c 80', pos=(1,0))
G.add_node('d 47', pos=(6,5))
G.add_node('e 97', pos=(5,6))
G.add_node('f 100', pos=(8,2))
G.add_edges_from(
    [('f 100', 'd 47'), ('f 100', 'e 97'), ('b 31', 'c 80')])

val_map = {'a 47': 1.0,'c 80': 1.0,'f 100':1.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

pos=nx.get_node_attributes(G,'pos')

nx.draw(G, cmap=plt.get_cmap('coolwarm'), pos=pos, node_color=values, with_labels=True, font_color='black', node_size=[1000,1000,1000,1000,1000,1000])
plt.show()