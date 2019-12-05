import random
import numpy as np
import networkx as nx
import time
import math

from tsp import travelingSalesman, getWeight
from cluster import MST, kcenter
from cluster_solver2 import solve, score

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
print("start")

t0 = time.time()
# print(kcenter(graph, homes, 0, 100))
# a = travelingSalesman(graph, homes + [0], 0)
tour, clusters = solve(graph, homes, 0)
print(time.time() - t0)
print(clusters)
print(score(graph, clusters, 0))

