import time
from gra_math.nullification import Nullifier
import numpy as np

nullifier = Nullifier()
data = np.random.rand(1000)
start = time.time()
for _ in range(100):
    nullifier.forward(data)
end = time.time()
print(f"Nullification benchmark: {(end-start)/100:.6f} sec per call")
