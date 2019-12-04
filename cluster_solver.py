import networkx as nx
from cluster import kcenter, travelingSalesman, getWeight

def solve(list_of_homes, start, G, params=[]):
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
    def total_dis(center, cluster):
        sum = 0
        for v in cluster:
            sum += getWeight(G, center, v)
        return sum
    
    set_clusters = []
    changeable_clusters = list(kcenter(G, list_of_homes, first_center=start))

    while changeable_clusters:
        clus = changeable_clusters.pop(0)
        if len(clus[1]) == 1:
            set_clusters.append(clus)
            continue
        new1, new2 = kcenter(G, clus[1], start if clus[0]==start else None)
        if total_dis(*new1) + total_dis(*new2) + 2 * getWeight(G, new1[0], new2[0]) / 3 < total_dis(*clus):
            changeable_clusters.append(new1)
            changeable_clusters.append(new2)
        else:
            set_clusters.append(clus)
    
    vertices = [clus[0] for clus in set_clusters]
    raopath = travelingSalesman(G, vertices, start)
    homes_dict = {clus[0]: clus[1] for clus in set_clusters}

    #its easy from here

    

