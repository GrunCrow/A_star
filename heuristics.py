def dijkstra():
    return 0


def heuristic_1(graph, node_index):     # number of children
    node_node = graph.nodes[node_index]
    node = node_node.get_name()

    children = graph.get_children(node)
    num_children = len(children)

    return int(num_children)


def heuristic_2(graph, node_index):     # number of parents
    node_node = graph.nodes[node_index]
    node = node_node.get_name()

    parents = graph.get_parents(node)
    num_parents = len(parents)

    return int(num_parents)


def heuristics(graph, node_index, heuristic):

    if heuristic == 1:
        h = heuristic_1(graph, node_index)
    elif heuristic == 2:
        h = heuristic_2(graph, node_index)
    else:
        h = dijkstra()

    return h
