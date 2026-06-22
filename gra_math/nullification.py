from .operators import Operator
import numpy as np

class Nullifier(Operator):
    def __init__(self, rate=0.1):
        self.rate = rate
    def forward(self, x):
        x = np.array(x)
        return x - self.rate * (x - np.mean(x))
    def idempotent_check(self, x):
        return np.allclose(self.forward(self.forward(x)), self.forward(x))
