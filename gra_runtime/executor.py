class Executor:
    def run(self, task):
        return task["fn"]()
