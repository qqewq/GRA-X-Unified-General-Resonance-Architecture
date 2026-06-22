class Workflow:
    def __init__(self):
        self.steps = []
    def add_step(self, name, agent, input_data=None):
        self.steps.append((name, agent, input_data))
    def execute(self):
        results = {}
        for name, agent, inp in self.steps:
            results[name] = agent.run(inp or results)
        return results
