class Node(object):

    def __init__(self, name, weight, predecessor_weight=0):
        self.name = name
        self.weight = weight
        self.predecessor_weight = predecessor_weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def set_predecessor_weight(self, weight):
        self.predecessor_weight = max(self.predecessor_weight, weight)

    def get_predecessor_weight(self):
        return self.predecessor_weight

    def __str__(self):
        return self.name

