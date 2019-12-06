import networkx as nx
from cluster import MST, kcenter, getWeight



def travelingSalesman(G, vertices, start):
    """
    Christofides' algorithm to approximate tsp
    """
    vertices = vertices[:]
    vertices = list(set(sorted(vertices)))
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
    assert nx.is_eulerian(mst_graph)
    for u, v in nx.eulerian_circuit(mst_graph, source=start):
        if u not in seen:
            ret.append(u)
            seen.add(u)
    ret.append(start)
    return ret
