import ray

@ray.remote
class DistributedWorker:
    def work(self, fn, *args):
        return fn(*args)

class DistributedRuntime:
    def __init__(self):
        ray.init(ignore_reinit_error=True)
    def submit(self, fn, *args):
        return DistributedWorker.remote().work.remote(fn, *args)
