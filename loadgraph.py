
import os

from graph import *
from node import Node


def show_files():
    # show files:
    print("Showing files name available:")
    for filename in os.listdir("data"):
        print(filename)


def ask_filename():
    # ask for filename
    filename = input("Enter file name: ")
    while not os.path.exists(f"data\\{filename}"):
        print("Invalid filename\n")
        filename = input("Enter file name: ")
    return filename


def getsize(filename):
    # open file
    with open("data//" + filename, "r") as file:
        lines = file.readlines()
    return lines.len()


def open_and_read(filename):
    # open file
    with open("data//" + filename, "r") as file:
        lines = file.readlines()

    '''
    count = 0
    for line in lines:
        count += 1
        print(f'line {count}: {line}')
    '''

    return lines


def build_graph(lines, number_of_nodes):

    graph = DiGraph()

    # create nodes
    for n_node in range(0, int(number_of_nodes)):
        node = Node(str(n_node), float(lines[n_node+1]))
        graph.add_node(node)

    # create edges
    for n_node in range(0, int(number_of_nodes)):
        src = n_node
        # children
        child_nodes = lines[n_node + int(number_of_nodes) + 1]
        child_node = child_nodes.split()
        for child in child_node:
            # child = int(child)
            if child != '-1':
                # print("Child node ", n_node, ": ", child)
                dest = child
                edge = Edge(str(src), str(dest))
                graph.add_edge(edge)

    return graph


def add_start_end_nodes(graph):

    # create nodes list
    nodes = set([])
    for n_node in range(0, graph.get_number_of_nodes()):
        node = graph.nodes[n_node]
        nodes.add(node.get_name())

    graph.set_start_end_flag(True)

    start_node = Node('Start', float(0))
    end_node = Node('End', float(0))

    graph.add_node(start_node)
    graph.add_node(end_node)

    # if no children node -> end_node
    for src in graph.nodes[:-2]:  # [:-2] take all elem of graph.nodes but 2 last ones (start and end nodes) //src=node
        if not graph.edges[src]:    # if no children
            edge = Edge(src.get_name(), end_node.get_name())
            graph.add_edge(edge)

        for dest in graph.edges[src]:  # dest = node
            if dest in nodes:
                nodes.remove(dest)

    # if no predecessor start_node -> node
    for n_node in nodes:
        edge = Edge(start_node.get_name(), str(n_node))
        graph.add_edge(edge)


def test():
    show_files()
    filename = ask_filename()

    lines = open_and_read(filename)

    number_of_nodes = lines[0]    # get number of nodes of the graph

    graph = build_graph(lines, number_of_nodes)

    # add_start_end_nodes(graph)

    '''node = '1'

    children = graph.get_children(node)

    print('The children in the graph for node: ', node, ' are')
    print(children)'''

    '''print()
    print('The nodes and edges in the graph are:')
    print(graph)'''

    return graph
