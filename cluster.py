import random
import numpy as np
import networkx as nx
import math

"""

@SEO MAYBE THIS WILL BE GOOD ?????
https://www.geeksforgeeks.org/k-centers-problem-set-1-greedy-approximate-algorithm/
see if someone else implemented it online and copy/cite



"""


def kcenter(G, vertices, first_center=None, clusters=2):
    """
    Input:
        G: graph of the nodes we want to cluster
        vertices: cluster the vertices in vertices to two groups
        k: always just do 2??
        first_center: if we want to specify the first center that should be randomly chosen
    Output:
        output 2 lists: each list holds the center vertex, and 
        [center 1, cluster 1], [center 2,  cluster 2]
    """

    pass

def MST(G, vertices):
    """
    output the edges of the mst of ONLY the vertices in vertices
    """
    H = nx.minimum_spanning_tree(G.subgraph(vertices), weight="weight")
    return H.edges(data=True)