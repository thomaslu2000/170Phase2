from pulp import *
import networkx as nx

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
    # create graph of only homes

    prob = LpProblem("Drive TAs Home", LpMinimize)
    newG = nx.DiGraph()
    newG.add_nodes_from(G)

    for edge in G.edges():
        fro = edge[0]
        to = edge[1]
        de = G.edge[fro][to]]['weight']

        rleft = pulp.LpVariable('rleft', lowBound=0, upBound = 1, cat='Integer')
        newG.add_edge(fro, to, rleft)

        rright = pulp.LpVariable('rright', lowBound=0, upBound = 1, cat='Integer')
        newG.add_edge(to, fro, rright)

        tleft = pulp.LpVariable('tleft', lowBound=0, cat='Integer')
        newG.add_edge(fro, to, tleft)

        tright = pulp.LpVariable('tright', lowBound=0, cat='Integer')
        newG.add_edge(to, fro, tright)

        prob += de * ((rleft + rright) * 2 / 3 + tleft + tright), "Total Cost of Path"
        # G.edge[edge[0]][edge[1]]['weight']
    prob.solve()
