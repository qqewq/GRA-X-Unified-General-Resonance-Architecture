class Pipeline:
    def __init__(self, steps):
        self.steps = steps
    def run(self, input_data):
        state = input_data
        for step in self.steps:
            state = step(state)
        return state
