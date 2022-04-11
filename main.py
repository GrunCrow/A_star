# libraries
import os
import time

# graph
import loadgraph

# algorithm
import algorithm

start = 'Start'
end = 'End'

print('=============================================')
for filename in os.listdir("data"):
    print('            ', filename)

    # load graph
    lines = loadgraph.open_and_read(filename)
    number_of_nodes = lines[0]  # get number of nodes of the graph
    graph = loadgraph.build_graph(lines, number_of_nodes)
    loadgraph.add_start_end_nodes(graph)

    start_index = graph.get_start_index()
    start_node = graph.nodes[start_index]
    end_index = graph.get_end_index()
    end_node = graph.nodes[end_index]

    print('-----------------------------------------')

    # algorithm with h(n) = 0 -> Dijkstra
    heuristic = 0
    start_time = time.time()
    algorithm.algorithm(graph, start, heuristic)
    end_time = time.time()
    dij = end_node.get_predecessor_weight() + end_node.get_weight()
    print('   Dijkstra')
    print('Execution time: ', end_time-start_time)
    print('Time (Solution): ', dij)

    print('-----------------------------------------')

    # algorithm with heuristic_1 -> number of children
    heuristic = 1
    start_time = time.time()
    algorithm.algorithm(graph, start, heuristic)
    end_time = time.time()
    h_1 = end_node.get_predecessor_weight() + end_node.get_weight()
    print('   Heuristic 1: Number of children')
    print('Execution time: ', end_time - start_time)
    print('Time (Solution): ', h_1)

    print('-----------------------------------------')

    # algorithm with heuristic_2 -> number of parents
    heuristic = 2
    start_time = time.time()
    algorithm.algorithm(graph, start, heuristic)
    end_time = time.time()
    h_2 = end_node.get_predecessor_weight() + end_node.get_weight()
    print('   Heuristic 2: Number of parents')
    print('Execution time: ', end_time - start_time)
    print('Time (Solution): ', h_2)

    print('=============================================')

'''print('=============================================')
filename = 'test_medium_sparse.dag'
print('            ', filename)
lines = load_graph.open_and_read(filename)
number_of_nodes = lines[0]  # get number of nodes of the graph
graph = load_graph.build_graph(lines, number_of_nodes)
load_graph.add_start_end_nodes(graph)
dij = dijkstra.test(graph, start_node)
print('Dijkstra time: ', dij)
a_star = 0
# a_star = a_star.main(graph, start_node, end_node)
print('A_star time: ', a_star)
print('=============================================')'''
