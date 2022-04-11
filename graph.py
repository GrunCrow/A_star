
from edge import Edge


class DiGraph(object):
    # nodes is a list of the nodes in the graph
    # edges is a dict mapping each node to
    # a list of its children

    def __init__(self):
        self.number_of_nodes = 0

        self.nodes = []     # all nodes = list
        self.edges = {}

        self.added_start_end = False

    def get_number_of_nodes(self):
        if self.added_start_end is False:
            return self.number_of_nodes
        else:
            return self.number_of_nodes-2

    def set_number_of_nodes(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes

    def set_start_end_flag(self, flag):
        self.added_start_end = flag

    def get_start_end_flag(self):
        return self.added_start_end

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('Duplicated Node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
            self.number_of_nodes += 1

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in (n.name for n in self.nodes) and dest in (n.name for n in self.nodes)):
            raise ValueError('Node not in graph')

        if src == 'Start':
            src = self.get_start_index()
        elif src == 'End':
            src = self.get_end_index()

        self.edges[self.nodes[int(src)]].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def get_children(self, node):
        children = []

        if node == 'Start':
            node = self.nodes[self.get_start_index()]
        elif node == 'End':
            node = self.nodes[self.get_end_index()]
        else:
            node = self.nodes[int(node)]

        for child in self.edges[node]:  # dest = node
            children.append(child)

        return children

    def get_parents(self, node):
        parents = []

        if node == 'Start':
            node = self.nodes[self.get_start_index()]
        elif node == 'End':
            node = self.nodes[self.get_end_index()]
        else:
            node = self.nodes[int(node)]

        for parent in self.nodes:
            for child in self.edges[parent]:
                if child == node.get_name():
                    parents.append(parent.get_name())
        return parents

    def get_start_index(self):
        if self.get_start_end_flag():
            index = self.get_number_of_nodes()
        else:
            raise ValueError('No Start Node')
        return index

    def get_end_index(self):
        if self.get_start_end_flag():
            index = self.get_number_of_nodes()+1
        else:
            raise ValueError('No End Node')
        return index

    def __str__(self):
        result = ''
        for src in self.nodes:  # src = node
            for dest in self.edges[src]:  # dest = node
                result += f"{src.get_name()}-->{dest}\n"
        return result[:-1]  # remove last newline


class Graph(DiGraph):

    def add_edge(self, edge):
        DiGraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        DiGraph.add_edge(self, rev)
