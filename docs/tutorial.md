# Quick Tutorial

1. Install: `pip install gra-x`
2. Create a nullification pipeline:
```python
from gra_math.nullification import Nullifier
n = Nullifier()
result = n.forward([0.1, 0.9, 0.5])
```
3. Run an LLM swarm:
```python
from examples.llm_swarm import run_swarm
answer = run_swarm("Explain quantum computing")
```
