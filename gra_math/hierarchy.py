from .operators import Operator

class Hierarchy(Operator):
    def __init__(self, levels):
        self.levels = levels
    def forward(self, x):
        # apply hierarchical refinement
        for level in self.levels:
            x = level(x)
        return x
