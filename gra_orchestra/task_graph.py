import networkx as nx

class TaskGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
    def add_task(self, name, deps=None):
        self.graph.add_node(name)
        if deps:
            for d in deps:
                self.graph.add_edge(d, name)
