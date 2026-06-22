class SubjectSwapper:
    def __init__(self, initial_agent):
        self.current = initial_agent
    def swap(self, new_agent):
        self.current = new_agent
        return self.current
