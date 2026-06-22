class Scheduler:
    def schedule(self, tasks):
        return sorted(tasks, key=lambda t: t["priority"])
