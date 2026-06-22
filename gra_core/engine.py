from .kernel import Kernel
from .state import State

class Engine:
    def __init__(self, kernel: Kernel):
        self.kernel = kernel
    def execute(self, state: State):
        return self.kernel.apply(state)
