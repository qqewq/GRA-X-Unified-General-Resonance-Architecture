from gra_swarm import Planner, Worker, Critic, Judge, Consensus

def run_swarm(question):
    planner = Planner()
    plan = planner.plan(question)
    worker = Worker()
    critic = Critic()
    judge = Judge()
    outputs = []
    for step in plan["steps"]:
        out = worker.execute(step)
        ev = critic.evaluate(out)
        outputs.append(ev)
    best = judge.decide(outputs)
    consensus = Consensus()
    final = consensus.reach([best["feedback"]])
    return final

if __name__ == "__main__":
    print(run_swarm("What is resonance?"))
