from gra_swarm.consensus import Consensus

def test_consensus():
    c = Consensus()
    result = c.reach(["A", "B", "A"])
    assert result == "A"
