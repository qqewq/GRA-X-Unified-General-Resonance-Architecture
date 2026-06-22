class EmotionModel:
    def __init__(self):
        self.valence = 0.0
        self.arousal = 0.0
    def update(self, stimulus):
        self.valence += stimulus.get("valence", 0)
        self.arousal += stimulus.get("arousal", 0)
