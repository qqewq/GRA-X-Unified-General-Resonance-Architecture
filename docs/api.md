# API Reference

All components share a common interface:
- `initialize()`
- `forward(input)`
- `backward(gradient)`
- `metric() -> dict`
- `state() -> dict`

Import example:
```python
from gra import Nullification, Resonance, Subject, Swarm, Orchestra
```
