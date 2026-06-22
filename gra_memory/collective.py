class CollectiveMemory:
    def __init__(self):
        self.shared = {}
    def write(self, agent_id, data):
        self.shared[agent_id] = data
    def read(self):
        return self.shared
