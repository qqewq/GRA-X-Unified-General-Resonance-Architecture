from .operators import Operator

class Chirality(Operator):
    def __init__(self, orientation=1):
        self.orientation = orientation  # +1 or -1
    def forward(self, x):
        return [self.orientation * v for v in x]
