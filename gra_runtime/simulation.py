class Simulation:
    def __init__(self, world):
        self.world = world
        self.time = 0
    def step(self):
        self.time += 1
        self.world.update()
