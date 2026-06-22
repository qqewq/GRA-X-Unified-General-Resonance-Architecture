class Judge:
    def decide(self, evaluations):
        best = max(evaluations, key=lambda e: e["score"])
        return best
