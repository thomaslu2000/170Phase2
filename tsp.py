import random
import numpy as np
import networkx as nx
import math
from cluster import MST, kcenter, getWeight



def travelingSalesman(G, vertices, start):
    """
    Christofides' algorithm to approximate tsp
    """
    mst_edges = MST(G, vertices)
    mst_graph = nx.MultiGraph()
    mst_graph.add_nodes_from(vertices)
    mst_graph.add_edges_from(mst_edges)
    
    O = []
    for v in vertices:
        if mst_graph.degree(v) % 2 == 1:
            O.append(v)
    
    m = G.subgraph(O).copy()
    for u, v, data in m.edges(data=True):
        data['weight'] *= -1
    
    P = nx.algorithms.matching.max_weight_matching(m, maxcardinality=True, weight="weight")
    for u, v in P:
        a = len(mst_graph.edges())
        mst_graph.add_edge(u, v, weight=getWeight(G, u, v))
    
    ret = []
    seen = set()
    for u, v in nx.eulerian_circuit(mst_graph, source=start):
        if u not in seen:
            ret.append(u)
            seen.add(u)
    ret.append(start)
    mst_size = sum([d["weight"] for u, v, d in mst_edges])
    return ret
