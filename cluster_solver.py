import random
import numpy as np
import networkx as nx
from cluster import cluster, findMiddle

def solve(list_of_homes, starting_car_location, G, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_homes: A list of homes indices in their integer form (for networkx)
        starting_car_location: The index of the starting location for the car
        G: the populated graph with edges and stuff
    Output:
        A list of locations representing the car path
        A dictionary mapping drop-off location to a list of homes of TAs that got off at that particular location
        NOTE: both outputs should be in terms of indices not the names of the locations themselves
    """
    curr_clusters = [list_of_homes]
    curr_centers = [findMiddle(G, list_of_homes)]

    new_clusters = []
    for verts in curr_clusters:
        new_clusters += cluster(G, verts)
    new_clusters = [findMiddle(G, clus) for clus in new_clusters]
    
    while (len(curr_centers) != len(new_centers)):
        pass
    
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
    vertices.remove(start)
    random.shuffle(vertices)
    for temperature in np.logspace(0,6,num=100000)[::-1]:
        [i,j] = sorted(random.sample(range(len(vertices)),2))

        old = getWeight(G, i, i+1, vertices) + getWeight(G, j-1, j, vertices)
        new = getWeight(G, j, i+1, newTour) + getWeight(G, j-1, i, newTour)
        
        if i == 0:
            old += getWeight(G, start, i, vertices)
            new += getWeight(G, start, j, newTour)
        else:
            old += getWeight(G, i - 1, i, vertices)
            new += getWeight(G, i - 1, j, newTour)

        if j == len(vertices) - 1:
            old += getWeight(G, j, start, vertices)
            new += getWeight(G, i, start, newTour)
        else:
            old += getWeight(G, j, j+1, vertices)
            new += getWeight(G, i, j+1, newTour)

        if math.exp( ( old - new) / temperature) > random.random():
            vertices = vertices[:i] + vertices[j:j+1] +  vertices[i+1:j] + vertices[i:i+1] + vertices[j+1:]
    return [start] + vertices + [start]

def getWeight(G, i, j, vertices):
    return G.get_edge_data(i, j)["weight"]