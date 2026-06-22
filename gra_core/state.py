from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class State:
    data: Any
    metadata: Dict = field(default_factory=dict)
    def update(self, new_data):
        self.data = new_data
    def get_metric(self):
        return {"size": len(str(self.data))}
