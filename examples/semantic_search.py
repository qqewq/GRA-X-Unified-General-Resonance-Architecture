from gra_semantic import Embedder, SemanticSpace
import numpy as np

embedder = Embedder()
space = SemanticSpace()
docs = ["GRA is a semantic architecture", "Nullification ensures stability", "Resonance aligns states"]
embeddings = embedder.embed(docs)
query = embedder.embed(["semantic stability"])[0]
distances = [space.distance(query, emb) for emb in embeddings]
print("Best match:", docs[np.argmin(distances)])
