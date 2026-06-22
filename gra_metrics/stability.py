def stability_score(sequence):
    return 1.0 / (1.0 + np.var(sequence))
