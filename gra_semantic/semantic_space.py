import numpy as np

class SemanticSpace:
    def __init__(self, dimension=384):
        self.dim = dimension
    def distance(self, v1, v2):
        return np.linalg.norm(v1 - v2)
