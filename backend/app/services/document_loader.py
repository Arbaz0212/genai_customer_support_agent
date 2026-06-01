import os

DOCS = []

def load_documents():
    global DOCS
    DOCS.clear()

    folder = "documents"

    if not os.path.exists(folder):
        os.makedirs(folder)

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                DOCS.append(f.read())

def get_docs():
    return DOCS
