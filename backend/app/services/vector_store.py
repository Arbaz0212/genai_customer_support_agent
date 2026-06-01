import faiss
import numpy as np

index = None
documents = []

def create_index(embeddings, docs):
    global index, documents
    documents = docs

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

def search(query_embedding, k=3):
    D, I = index.search(np.array([query_embedding]), k)
    return [documents[i] for i in I[0]]
