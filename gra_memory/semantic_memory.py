class SemanticMemory:
    def __init__(self):
        self.triples = []
    def add_fact(self, subj, pred, obj):
        self.triples.append((subj, pred, obj))
