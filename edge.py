class Edge(object):

    def __init__(self, src, dest):
        # src and dest are nodes
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src.get_name() + '-->' + self.dest.get_name()