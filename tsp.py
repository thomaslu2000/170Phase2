import random
import numpy as np
import networkx as nx
import math
from cluster import MST



def travelingSalesman(G, vertices, start):
    """
    Christofides' algorithm to approximate tsp
    """
    mst_edges = MST(G, vertices)
    print(mst_edges)
    mst_graph = nx.empty_graph(vertices)
    mst_graph.add_edges_from(mst_edges)
    
    O = []
    for v in vertices:
        if mst_graph.degree(v) % 2 == 1:
            O.append(v)
    
    m = G.subgraph(O)
    for u, v, data in m.edges(data=True):
        data['weight'] *= -1
    
    P = nx.algorithms.matching.max_weight_matching(m, weight="weight")
    for u, v in P:
        mst_graph.add_edge(u, v, weight=getWeight(G, u, v))
    
    euler = nx.eulerian_circuit(mst_graph)
    for r in euler:
        print(r)
    pass


def travelingSalesmanOld(G, vertices, start):
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
    coolingRate = 0.1
    if len(vertices) <= 1:
        return vertices

    min_span_edges = MST(G, vertices)
    min_span = sum([getWeight(G, e[0], e[1]) for e in min_span_edges])
    print("MST: ", min_span, " 2xMST: ", 2*min_span)
    
    try:
        vertices.remove(start)
    except ValueError:
        pass
    random.shuffle(vertices)
    temp = 10e8
    while (temp > 1):
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

        if math.exp( ( old - new) / temp) > random.random():
            vertices = vertices[:i] + vertices[j:j+1] +  vertices[i+1:j] + vertices[i:i+1] + vertices[j+1:]
        temp *= 1 - coolingRate
        if temp <= 1:
            score = getWeight(G, start, vertices[0]) + getWeight(G, vertices[-1], start)
            for i in range(len(vertices) - 1):
                score += getWeight(G, i, i+1, vertices)
            if score > 2* min_span:
                temp = 100
    return [start] + vertices + [start]

def getWeight(G, i, j, vertices=None):
    if i == j:
        return 0
    if vertices:
        return G.get_edge_data(vertices[i], vertices[j])["weight"]
    else:
        return G.get_edge_data(i, j)["weight"]