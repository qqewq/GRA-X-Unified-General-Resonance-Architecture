from .state import State

class Kernel:
    def __init__(self, operators=None):
        self.operators = operators or []
    def apply(self, state: State) -> State:
        for op in self.operators:
            state = op.forward(state)
        return state
