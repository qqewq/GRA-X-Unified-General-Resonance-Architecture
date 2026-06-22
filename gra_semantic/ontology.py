class Ontology:
    def __init__(self):
        self.concepts = {}
    def add_concept(self, name, parent=None):
        self.concepts[name] = parent
