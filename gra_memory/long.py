class LongMemory:
    def __init__(self):
        self.store = {}
    def save(self, key, value):
        self.store[key] = value
