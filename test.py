import random
import numpy as np
import networkx as nx
import time
import math

from tsp import travelingSalesman, getWeight
from cluster import MST

# # change this too
# items = 100

# V = np.random.randint(int(items * 9/10), items ) # vertices

# # name array thingy, pls change
# randnames = np.random.randint(1, 5600)
# names = [hex(i * randnames + randnames)[2:] for i in range(V + 1)]
# random.shuffle(names)



# homes = random.sample(range(V), np.random.randint(int(V / 3), int(items / 2) ))

# positions = np.random.rand(V, 2)
# differences = positions[:, None, :] - positions[None, :, :]
# distances = np.sqrt(np.sum(differences**2, axis=-1))
# distances = np.multiply(distances, 100)
# distances = np.around(distances, decimals=5)

# graph = nx.from_numpy_matrix(distances, create_using=nx.Graph())
# print("start")

# t0 = time.time()
# a = travelingSalesman(graph, homes, 0)
# print(time.time() - t0)
# print(sum([getWeight(graph, i, i+1, a) for i in range(len(a) - 1)]))


G = nx.complete_graph(8)

G = nx.Graph()

G.add_edge('a', 'b', weight=0.6)
G.add_edge('a', 'c', weight=0.2)
G.add_edge('c', 'd', weight=0.1)
G.add_edge('c', 'e', weight=0.7)
G.add_edge('c', 'f', weight=0.9)
G.add_edge('a', 'd', weight=0.3)
travelingSalesman(G, ['a', 'e', 'd', 'f'], 'a')

