import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

#G.add_node(1)
#G.add_nodes_from([2,4])
##G.node[1]['room'] = 714
#H=nx.path_graph(10)
#G.add_nodes_from(H)

G = nx.DiGraph()
G.add_edges_from([(1,2),(1,3),(1,4),(3,4)])
#G.add_node(H)

#G.add_edge(1,2)
#e=(2,3)
#G.add_edge(*e)

#G.add_edges_from([(1,2),(1,3)])

#G.add_edges_from(H.edges())
#G.degree([1,2])

nx.draw_circular(G)
plt.show()
pos = nx.spring_layout(G)
edge_labels[((1,2), (1,3))] = float(weight1)
nx.draw_networkx(G, pos=pos)

nx.draw_networkx_edge_labels(G, pos=pos, edge_labels='k')