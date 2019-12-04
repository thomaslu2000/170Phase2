import random
import numpy as np
import networkx as nx
import time
import math

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
    if vertices is not None:
        return G.get_edge_data(vertices[i], vertices[j])["weight"]
    else:
        return G.get_edge_data(i, j)["weight"]



# change this too
items = 200

V = np.random.randint(int(items * 9/10), items ) # vertices

# name array thingy, pls change
randnames = np.random.randint(1, 5600)
names = [hex(i * randnames + randnames)[2:] for i in range(V + 1)]
random.shuffle(names)



homes = random.sample(range(V), np.random.randint(int(V / 3), int(items / 2) ))

positions = np.random.rand(V, 2)
differences = positions[:, None, :] - positions[None, :, :]
distances = np.sqrt(np.sum(differences**2, axis=-1))
distances = np.multiply(distances, 100)
distances = np.around(distances, decimals=5)

graph = nx.from_numpy_matrix(distances, create_using=nx.Graph())

t0 = time.time()
travelingSalesman(graph, homes, 0)
print(time.time() - t0)

t0 = time.time()
travelingSalesman(graph, homes, 0)
print(time.time() - t0)

t0 = time.time()
travelingSalesman(graph, homes, 0)
print(time.time() - t0)
