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


def travelingSalesman(G, vertices, start):
    """
    Approximation algo for tsp modified from 
    https://ericphanson.com/blog/2016/the-traveling-salesman-and-10-lines-of-python/

    Input:
        G: The graph on which to tsp
        vertices: a list of the vertices on which to do tsp. start only appears once
        start: the vertex on which to start and end the tsp
    Output:
        A list of vertices to visit in order of visitation
    """
    if len(vertices) <= 1:
        return vertices
    try:
        vertices.remove(start)
    except ValueError:
        pass
    random.shuffle(vertices)
    for temperature in np.logspace(0,6,num=100000)[::-1]:
        [i,j] = sorted(random.sample(range(len(vertices)),2))

        old = getWeight(G, i, i+1, vertices) + getWeight(G, j-1, j, vertices)
        new = getWeight(G, j, i+1, vertices) + getWeight(G, j-1, i, vertices)
        
        if i == 0:
            old += getWeight(G, start, i, vertices)
            new += getWeight(G, start, j, vertices)
        else:
            old += getWeight(G, i - 1, i, vertices)
            new += getWeight(G, i - 1, j, vertices)

        if j == len(vertices) - 1:
            old += getWeight(G, j, start, vertices)
            new += getWeight(G, i, start, vertices)
        else:
            old += getWeight(G, j, j+1, vertices)
            new += getWeight(G, i, j+1, vertices)

        if math.exp( ( old - new) / temperature) > random.random():
            vertices = vertices[:i] + vertices[j:j+1] +  vertices[i+1:j] + vertices[i:i+1] + vertices[j+1:]
    return [start] + vertices + [start]

def getWeight(G, i, j, vertices=None):
    if i == j:
        return 0
    if vertices:
        return G.get_edge_data(vertices[i], vertices[j])["weight"]
    else:
        return G.get_edge_data(i, j)["weight"]