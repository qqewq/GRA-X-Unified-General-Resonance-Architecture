from pydantic import BaseModel

class Config(BaseModel):
    nullification_rate: float = 0.1
    resonance_threshold: float = 0.8
    max_hierarchy_depth: int = 5
