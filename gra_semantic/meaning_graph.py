import networkx as nx

class MeaningGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
    def add_relation(self, src, dst, weight=1.0):
        self.graph.add_edge(src, dst, weight=weight)
