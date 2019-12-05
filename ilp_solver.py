# from pulp import *
import networkx as nx
from ortools.graph import pywrapgraph
import math

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
    H = G.copy()
    next_index = G.number_of_nodes()
    for home in list_of_homes:
        H.add_edge(home, next_index, weight = 0)
        next_index += 1
    start_nodes = []
    end_nodes   = []
    capacities  = []
    unit_costs  = []

    supplies = [0] * H.number_of_nodes()
    supplies[starting_car_location] = len(list_of_homes)
    for home in list_of_hones:
        supplies[home] = -1

    for edge in H.edges():
        fro = edge[0]
        to = edge[1]
        de = G.edge[fro][to]]['weight']
        if fro in list_of_homes and to >= G.number_of_nodes(): # home to dummy nodes: only add TA edge in one direction
            start_nodes.append(fro)
            end_nodes.append(to)
            capacities.append(1)
            unit_costs.append(1)
        else:
            # forward & backward Rao node
            start_nodes.append(fro)
            end_nodes.append(to)
            capacities.append(de * 2 / 3)
            unit_costs.append(de * 2 / 3)

            start_nodes.append(to)
            end_nodes.append(fro)
            capacities.append(de * 2 / 3)
            unit_costs.append(de * 2 / 3)

            # forward & backward TA node
            start_nodes.append(fro)
            end_nodes.append(to)
            capacities.append(math.inf)
            unit_costs.append(de)

            start_nodes.append(to)
            end_nodes.append(fro)
            capacities.append(math.inf)
            unit_costs.append(de)

    # Instantiate a SimpleMinCostFlow solver.
    min_cost_flow = pywrapgraph.SimpleMinCostFlow()

    # Add each arc.
    for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i], capacities[i], unit_costs[i])

    # Add node supplies.
    for i in range(0, len(supplies)):
        min_cost_flow.SetNodeSupply(i, supplies[i])

    # Find the minimum cost flow tour.
    if min_cost_flow.Solve() == min_cost_flow.INFEASIBLE:
        return [], []

    arcs = {} # key: source node; value: list of (dest node, edge weight)
    for i in range(min_cost_flow.NumArcs()):
        if min_cost_flow.Flow(i) != 0:
            key = min_cost_flow.Tail(i)
            value = (min_cost_flow.Head(i), min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i))
            arcs[key] = arcs.get(key, []) + [value]


    car_path = []

    curr = starting_car_location
    car_path.append(curr)
    while curr in arcs:
        next = curr # set to none
        max = float("inf")
        for dest in arcs[curr]:
            if dest[1] < max:
                min = dest[1]
                next = dest[0]
        car_path.append(next)
        curr = next

    drop_offs = {}
    for stop in car_path:
        homes = []
        for dest in arcs[stop]:
            if dest[0] in list_of_homes:
                homes.append(dest[0])
        drop_offs[stop, homes]

    return car_path, drop_offs


    # -------------------- OLD STUFF

    # create graph of only homes

    # prob = LpProblem("Drive TAs Home", LpMinimize)
    # newG = nx.DiGraph()
    # newG.add_nodes_from(G)

    # for edge in G.edges():
    #     fro = edge[0]
    #     to = edge[1]
        # de = G.edge[fro][to]]['weight']

        # rleft = pulp.LpVariable('rleft', lowBound=0, upBound = 1, cat='Integer')
        # newG.add_edge(fro, to, capacity = 1.0)

        # rright = pulp.LpVariable('rright', lowBound=0, upBound = 1, cat='Integer')
        # newG.add_edge(to, fro, capacity = 1.0)

        # tleft = pulp.LpVariable('tleft', lowBound=0, cat='Integer')
        # newG.add_edge(fro, to, capacity = inf)

        # tright = pulp.LpVariable('tright', lowBound=0, cat='Integer')
        # newG.add_edge(to, fro, capactiy = inf)

        # prob += de * ((rleft + rright) * 2 / 3 + tleft + tright), "Total Cost of Path"

        # G.edge[edge[0]][edge[1]]['weight']
        # R[u][v]['flow'] == -R[v][u]['flow']
    # prob.solve()
    # flow_value, flow_dict = nx.maximum_flow(newG, starting_car_location, starting_car_location)
    # car_path = []
    # curr = starting_car_location
    # car_path.append(curr)
    # while flow_dict[curr]:
    #     next = null
    #     min = float("-inf")
    #     for to in flow_dict[curr]:
    #         if flow_dict[curr][to] > min:
    #             min = flow_dict[curr][to]
    #             next = to
    #     car_path.append(next)
    #     curr = next
    # car_path.reverse()
    # return car_path
