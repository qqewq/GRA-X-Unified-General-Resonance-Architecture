class Router:
    def route(self, task_type):
        mapping = {"plan": "planner", "execute": "worker", "review": "critic"}
        return mapping.get(task_type, "worker")
