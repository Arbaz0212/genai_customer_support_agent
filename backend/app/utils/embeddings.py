from sentence_transformers import SentenceTransformer
import numpy as np

# load embedding model once
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed(texts):
    """
    Convert list of texts into embedding vectors
    """
    vectors = model.encode(texts)
    return np.array(vectors).astype("float32")
