from heuristics import heuristics


def get_node_index(graph, node):    # node = str
    node_index = node
    if node == 'Start':
        node_index = graph.get_start_index()
    if node == 'End':
        node_index = graph.get_end_index()

    return int(node_index)   # return int


def algorithm(graph, start_node, heuristic=0):
    visited = []
    to_visit = [start_node]

    while len(to_visit) > 0:
        current = to_visit[0]
        current_index = get_node_index(graph, current)
        current_node = graph.nodes[current_index]

        for node in to_visit:
            node_index = get_node_index(graph, node)
            node_node = graph.nodes[int(node_index)]

            h = heuristics(graph, node_index, heuristic)
            if (node_node.get_weight() + h) > (current_node.get_weight() + h):  # if (node_node.get_weight() + h) < (current_node.get_weight() + h):
                current = node
                current_index = get_node_index(graph, current)
                current_node = graph.nodes[current_index]

        assert current_node is not None
        assert current_node not in visited

        to_visit.remove(current)
        visited.append(current)

        children = graph.get_children(current)
        for child in children:
            child_index = get_node_index(graph, child)
            child_node = graph.nodes[child_index]

            # calculate distance from present node till target node
            child_node.set_predecessor_weight(current_node.get_weight() + current_node.get_predecessor_weight())

        # Iterating through the child nodes of current_node
        for child in children:
            # child_index = get_node_index(graph, child)
            # child_node = graph.nodes[child_index]

            #assert child not in to_visit
            #assert child not in visited

            '''parents = graph.get_parents(child)
            if all(parent in visited for parent in parents):
                to_visit.append(child)'''
            if child not in visited and child not in to_visit:
                to_visit.append(child)                                          # MODIFICATION

    assert len(to_visit) == 0
    nodes = graph.nodes
    for node in nodes:
        assert str(node) in visited
    assert graph.nodes[0].get_predecessor_weight() == 0


def test(graph, start_node):

    return algorithm(graph, start_node)

    # print("Total time: ", dij)
