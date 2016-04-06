"""
Author:    Agnieszka Gancarczyk
File:      kingchicken.py
Practical: Weighted Graphs
Brief:     Class represents a solution to a King Chicken problem given.
"""

from __future__ import print_function, division
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def generate_farmyard(n):
    """Returns a digraph representing a farmyard of $n$ chickens.
        There should be $2^{n(n+1)/2}$ such digraphs so the search
        space gets large very quickly."""

    new_g = nx.DiGraph()

    new_g.add_nodes_from(range(n))
    for node in new_g.nodes():
        for otherNode in new_g.nodes():
            if not new_g.has_edge(node, otherNode) and not new_g.has_edge(otherNode, node) and node != otherNode:
                if bool(random.getrandbits(1)):
                    new_g.add_edge(node, otherNode)
                else:
                    new_g.add_edge(otherNode, node)
    return new_g

def has_king_chicken(g):
    """Returns True if the digraph, d contains a king chicken."""

    for node in g.nodes(data=False):
        virtually_pecked = list()
        adjacent = g.successors(node)
        virtually_pecked.extend(adjacent)
        for adj in adjacent:
            one_deg = g.successors(adj)
            virtually_pecked.extend(one_deg)

        nodes = g.nodes()
        nodes.remove(node)
        if set(virtually_pecked) == set(nodes):
            return True

    return False

count = 0
while count < 100:                     #<--replace 100 by bigger value
    count += 1
    n = np.random.randint(100, 10000)  #random integer in range 2..10000
    g = generate_farmyard(n)           #generate digraph
    print('Testing graph of size n=', n)
    if not has_king_chicken(g):
        print ('Pay me the money!')
        pos = nx.spring_layout(g, k=1, iterations=100)
        nx.draw_networkx_nodes(g, pos, node_size=500)

        labels = {v: v for v in g.nodes() }           #get label dict from graph
        nx.draw_networkx_labels(g, pos, labels=labels)

        nx.draw_networkx_edges(g, pos)

        plt.show()
