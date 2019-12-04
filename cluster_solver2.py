import networkx as nx
from cluster import kcenter, travelingSalesman, getWeight


def solve(list_of_homes, start, G, repeat=2, params=[]):
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
    old_val, old_tour = solve(G, old_clusters, start)
    best_val, best_tour, best_clusters = old_val, old_tour, old_clusters

    new_val, new_tour, new_clusters = getNew(G, list_of_homes, start, 2, repeat)
    k = 3
    cont = int(len(list_of_homes) / 20)
    if new_val < old_val:
        cont -= 1

    while (k <= len(list_of_homes) and cont > 0):
        old_val, old_tour, old_clusters = new_val, new_tour, new_clusters
        if old_val < best_val:
            best_val, best_tour, best_clusters = old_val, old_tour, old_clusters
        new_clusters = kcenter(G, list_of_homes, first_center=start, clusters=k)
        new_val, new_tour = solve(G, new_clusters, start)
        k += 1
        if new_val < old_val:
            cont -= 1

    
    return best_tour, {c[0]: c[1] for c in best_clusters}

def getNew(G, homes, start, k, repeat):
    best_clusters = kcenter(G, list_of_homes, first_center=start, clusters=k)
    best_val, best_tour = solve(G, best_clusters, start)
    for i in range(repeat - 1):
        next_clusters = kcenter(G, list_of_homes, first_center=start, clusters=k)
        next_val, next_tour = solve(G, next_clusters, start)
        if next_val < best_val:
            best_val, best_tour, best_clusters = next_val, next_tour, next_clusters
    return best_val, best_tour, best_clusters

            

def solve(G, clusters, start):
    sum = 0
    tour = travelingSalesman(G, [c[0] for c in clusters], start)
    for i in range(len(tour) - 1)
        sum += getWeight(G, i, i+1, tour)
    for c in clusters:
        for home in c[1]:
            sum += getWeight(G, home, c[0])
    return sum, tour
