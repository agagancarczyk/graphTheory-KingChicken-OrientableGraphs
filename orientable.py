"""
Author:    Agnieszka Gancarczyk
File:      orientable.py
Practical: Weighted Graphs
Brief:     Class represents a solution to an orientable graph problem given.
"""

#from __future__ import print_function, division
import networkx as nx
import matplotlib.pyplot as plt
import random


def generate_orientation(g):
    """Return a digraph resulting from assigning an orientation to each edge in graph $g$."""
    dir = g.to_directed()
    edges = dir.edges()

    for e in edges:
        if dir.has_edge(e[1], e[0]):
            if bool(random.getrandbits(1)):
                t = (e[0], e[1])
            else:
                t = (e[1], e[0])
            edges.remove(t)
            dir.remove_edge(t[0], t[1])

    return dir
    pass

def is_orientable(g):
    """Retuen __True__ iff the given graph, $g$, is orientable."""
    return nx.is_strongly_connected(g)
    pass

#hard to generate a strongly connected graph randomly
#g = nx.gn_graph(6).to_undirected()

#strongly connected by hand
g = nx.DiGraph()
g.add_nodes_from([0,1,2,4])
g.add_path([0,1,2,3,4,0])
g.add_path([1,3])


pos = nx.spring_layout(g, k=1, iterations=100)
nx.draw_networkx_nodes(g, pos, node_size=500)
labels = {v: v for v in g.nodes() }                 #get label dict from graph
nx.draw_networkx_labels(g, pos, labels=labels)
nx.draw_networkx_edges(g, pos)


digraph = generate_orientation(g)
orientable = is_orientable(digraph)
i = 0
while not orientable:
    i += 1
    digraph = generate_orientation(g)
    orientable = is_orientable(digraph)
    print("{} {} {}".format(i, "\t\t" , orientable))
print(orientable)
plt.show()
