class GoalManager:
    def __init__(self):
        self.goals = []
    def add_goal(self, description, priority):
        self.goals.append({"desc": description, "priority": priority})
