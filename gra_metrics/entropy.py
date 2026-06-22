import numpy as np
def semantic_entropy(probs):
    return -np.sum(probs * np.log(probs + 1e-10))
