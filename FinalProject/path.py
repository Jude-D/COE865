import json

def initialize_paths(tree, start_node):
    # Initialize each node to infinity
    minimum_costs = {}
    for node in tree:
        minimum_costs[node] = 999
    minimum_costs[start_node] = 0

    return minimum_costs

def get_SPT_list(minimum_costs, next_hops, start_node):
    shortest_paths = {}
    for node in minimum_costs:
        if node == start_node:
            shortest_paths[node] = (minimum_costs[node], node)
        else:
            shortest_paths[node] = (minimum_costs[node], next_hops[node])

    return shortest_paths

def dijkstra(tree, start_node, residual_credits_N2=0, residual_credits_N3=0):
    # Initialize next-hops and visited nodes
    next_hops = {}
    established_nodes = {}

    # Initialize each node to infinity
    minimum_costs = initialize_paths(tree, start_node)

    # Iterate through each node
    curr_node = start_node
    while curr_node is not None:
        neighbor_nodes = tree[curr_node]
        for node, cost in neighbor_nodes.items():
            if node not in established_nodes.keys():
                # Check if current node cost + link cost is less than shortest path cost of neighbour
                if minimum_costs[curr_node] + cost < minimum_costs[node]:
                    minimum_costs[node] = minimum_costs[curr_node] + cost
                    next_hops[node] = curr_node
                    # Choose forwarder node based on residual credit system
                    if node == 'N5' and curr_node in ['N2', 'N3'] and residual_credits_N2 > residual_credits_N3:
                        minimum_costs
                        next_hops[node] = 'N2'
        
        # Add to established nodes (shortest path found)
        established_nodes[curr_node] = minimum_costs[curr_node]

        # Move to next node
        unestablished_nodes = {key: minimum_costs[key] for key, value in set(minimum_costs.items()).difference(established_nodes.items())}
        curr_node = min(unestablished_nodes, key=unestablished_nodes.get, default=None)
    return get_SPT_list(minimum_costs, next_hops, start_node)

def get_minimum_cost_tree(start_node='N1', residual_credits_N2=0, residual_credits_N3=0):
    tree = {}
    with open("configs\\topology.json", "r") as f:
        tree = json.load(f)
    return dijkstra(tree, start_node, residual_credits_N2, residual_credits_N3)

def get_full_path(start_node, source_node, shortest_paths):
    path = [start_node]
    curr_node = start_node
    while curr_node != source_node:
        curr_node = shortest_paths[curr_node][1]
        path.append(curr_node)

    return path

def get_next_nodes(tree, node_of_interest):
    nodes = []
    for node in tree:
        next_hop = tree[node][1]
        if next_hop == node_of_interest:
            nodes.append(node)

    return nodes