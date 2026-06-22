from .operators import Operator
import numpy as np

class Resonance(Operator):
    def forward(self, states):
        a, b = states
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    def metric(self):
        return {"type": "cosine_similarity"}
