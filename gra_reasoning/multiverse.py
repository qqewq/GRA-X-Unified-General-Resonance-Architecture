class MultiverseReasoner:
    def generate_worlds(self, state, n=5):
        return [state + f"_world_{i}" for i in range(n)]
    def select_best(self, worlds, evaluator):
        return max(worlds, key=evaluator)
