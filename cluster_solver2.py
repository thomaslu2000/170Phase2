import networkx as nx
from cluster import kcenter
from tsp import travelingSalesman, getWeight

def solve(list_of_homes, start, G, repeat=1, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_homes: A list of homes indices in their integer form (for networkx)
        start: starting_car_location, The index of the starting location for the car
        G: the populated graph with edges and stuff
    Output:
        A list of locations representing the car path
        A dictionary mapping drop-off location to a list of homes of TAs that got off at that particular location
        NOTE: both outputs should be in terms of indices not the names of the locations themselves
    
    """
    old_clusters = [ [start, list_of_homes] ]
    old_val, old_tour = score(G, old_clusters, start)
    best_val, best_tour, best_clusters = old_val, old_tour, old_clusters

    for k in range(2, len(homes)):
        new_clusters = kcenter(G, list_of_homes, first_center=start, clusters=k)
        new_val, new_tour = score(G, new_clusters, start)
        if new_val < best_val:
            best_val, best_tour, best_clusters = new_val, new_tour, new_clusters
    
    return best_tour, {c[0]: c[1] for c in best_clusters}   
            

def score(G, clusters, start):
    val = 0
    tour = travelingSalesman(G, [c[0] for c in clusters], start)
    for i in range(len(tour) - 1)
        val += getWeight(G, i, i+1, tour)
    val *= 2 / 3
    for center, homes in clusters:
        for home in homes:
            val += getWeight(G, center, homes)
    return val, tour
