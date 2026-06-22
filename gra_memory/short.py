class ShortMemory:
    def __init__(self, size=7):
        self.buffer = [None]*size
        self.idx = 0
    def add(self, item):
        self.buffer[self.idx % len(self.buffer)] = item
        self.idx += 1
