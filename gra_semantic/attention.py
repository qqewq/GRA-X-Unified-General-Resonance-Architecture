import numpy as np

def attention(query, keys, values):
    scores = np.dot(query, keys.T)
    weights = np.exp(scores) / np.sum(np.exp(scores))
    return np.dot(weights, values)
