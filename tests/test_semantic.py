from gra_semantic.embedding import Embedder

def test_embedding_shape():
    e = Embedder()
    emb = e.embed(["hello"])
    assert emb.shape == (1, 384)
