from gra_math.nullification import Nullifier
from gra_metrics.stability import stability_score

class SelfHealingModel:
    def __init__(self):
        self.nullifier = Nullifier(rate=0.05)
        self.state = [0.8, 0.2, 0.9]
    def detect_anomaly(self):
        return stability_score(self.state) < 0.5
    def heal(self):
        self.state = self.nullifier.forward(self.state)
        print("Healed state:", self.state)

if __name__ == "__main__":
    model = SelfHealingModel()
    if model.detect_anomaly():
        model.heal()
