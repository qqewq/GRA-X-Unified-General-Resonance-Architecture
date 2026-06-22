class RecursiveReasoner:
    def solve(self, problem):
        if self.base_case(problem):
            return problem
        sub = self.decompose(problem)
        return self.combine([self.solve(s) for s in sub])
    def base_case(self, p): return len(p) < 2
    def decompose(self, p): return p[:len(p)//2], p[len(p)//2:]
    def combine(self, parts): return parts[0] + parts[1]
