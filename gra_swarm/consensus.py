class Consensus:
    def reach(self, opinions):
        # Simple majority voting
        return max(set(opinions), key=opinions.count)
