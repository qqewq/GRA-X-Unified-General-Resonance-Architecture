from gra_math.nullification import Nullifier
import numpy as np

def test_nullification_idempotent():
    n = Nullifier(rate=0.1)
    x = np.array([0.2, 0.8, 0.5])
    assert n.idempotent_check(x)

def test_resonance():
    from gra_math.resonance import Resonance
    r = Resonance()
    assert abs(r.forward([np.array([1,0]), np.array([1,0])]) - 1.0) < 0.001
