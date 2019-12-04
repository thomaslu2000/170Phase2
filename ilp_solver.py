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
    for every edge in G:
        de = orig edge weight
        rleft = pulp.LpVariable('rleft', lowBound=0, upBound = 1, cat='Integer')
        rright = pulp.LpVariable('rright', lowBound=0, upBound = 1, cat='Integer')
        tleft = pulp.LpVariable('tleft', lowBound=0, cat='Integer')
        tright = pulp.LpVariable('tright', lowBound=0, cat='Integer')
        prob += de * ((rleft + rright) * 2 / 3 + tleft + tright), "Total Cost of Path"
    prob.solve()
