from gra_swarm.consensus import Consensus
from gra_orchestra.workflow import Workflow

class Drone:
    def __init__(self, id):
        self.id = id
    def propose_route(self):
        return f"Route_{self.id}"

drones = [Drone(i) for i in range(3)]
consensus = Consensus()
routes = [d.propose_route() for d in drones]
final_route = consensus.reach(routes)
print("Agreed route:", final_route)
