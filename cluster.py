import networkx as nx
import math

def getWeight(G, i, j, vertices=None):
    if i == j:
        return 0
    if vertices:
        return G.get_edge_data(vertices[i], vertices[j])["weight"]
    else:
        return G.get_edge_data(i, j)["weight"]


def kcenter(G, homes, first_center, clusters):
    if clusters == len(homes) + 1:
        return [[home, [home]]  for home in homes]
    options = homes[:]
    if first_center in options:
        options.remove(first_center)
    cs = [first_center]
    for i in range(clusters - 1):
        next_clus = max(options, key=lambda v: min([getWeight(G, v, c) for c in cs]))
        cs.append(next_clus)
        options.remove(next_clus)

    d = {c:[] for c in cs}
    for home in homes:
        closest = min(cs, key=lambda x: getWeight(G, x, home))
        d[closest].append(home)
    return [[c, d[c]] for c in cs if d[c]]


def MST(G, vertices):
    """
    output the edges of the mst of ONLY the vertices in vertices
    """
    H = nx.minimum_spanning_tree(G.subgraph(vertices), weight="weight")
    return H.edges(data=True)