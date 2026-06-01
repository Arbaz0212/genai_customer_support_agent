import os
import numpy as np
from app.utils.embeddings import embed

DOCS_FOLDER = "documents"

documents = []
vectors = []


def chunk_text(text):
    # Split FAQ by numbered questions
    parts = text.split("\n\n")
    return [p.strip() for p in parts if len(p.strip()) > 20]


def load_documents():
    global documents, vectors
    documents = []
    vectors = []

    if not os.path.exists(DOCS_FOLDER):
        return

    for file in os.listdir(DOCS_FOLDER):
        path = os.path.join(DOCS_FOLDER, file)

        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

                chunks = chunk_text(text)

                for chunk in chunks:
                    documents.append(chunk)
                    vectors.append(embed(chunk))


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve_context(query: str):

    if not documents:
        load_documents()

    if not documents:
        return None

    query_vec = embed(query)

    best_score = 0
    best_doc = None

    for doc, vec in zip(documents, vectors):
        score = cosine_similarity(query_vec, vec)

        if score > best_score:
            best_score = score
            best_doc = doc

    if best_score < 0.40:
        return None

    return best_doc
