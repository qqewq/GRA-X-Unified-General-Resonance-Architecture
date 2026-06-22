from collections import deque

class SubjectiveMemory:
    def __init__(self, capacity=100):
        self.episodes = deque(maxlen=capacity)
    def store(self, event):
        self.episodes.append(event)
