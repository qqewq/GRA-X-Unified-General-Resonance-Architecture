from gra_runtime.scheduler import Scheduler

def test_scheduler():
    s = Scheduler()
    tasks = [{"priority": 2}, {"priority": 1}]
    ordered = s.schedule(tasks)
    assert ordered[0]["priority"] == 1
