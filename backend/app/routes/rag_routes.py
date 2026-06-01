from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from pydantic import BaseModel

from backend.app.services.rag import add_documents, search, list_documents
from backend.app.services.llm import generate_answer

router = APIRouter()


# =========================
# Request Model
# =========================
class ChatRequest(BaseModel):
    query: str


# =========================
# Upload Documents Endpoint
# =========================
@router.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    try:
        texts = []
        filenames = []

        for file in files:
            content = await file.read()
            if not content:
                continue

            text = content.decode(errors="ignore")
            texts.append(text)
            filenames.append(file.filename)

        if not texts:
            raise HTTPException(status_code=400, detail="No valid files uploaded")

        add_documents(texts)

        return {
            "status": "uploaded",
            "files": filenames,
            "count": len(texts)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =========================
# List Uploaded Documents
# =========================
@router.get("/documents")
async def documents():
    docs = list_documents()
    return {"documents": docs}


# =========================
# Chat Endpoint (FIXED)
# =========================
@router.post("/ai/chat")
async def chat_ai(request: ChatRequest):
    try:
        query = request.query

        # retrieve relevant context
        results = search(query, k=3)
        context = "\n".join(results)

        prompt = f"""
Answer the question ONLY using the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

        answer = generate_answer(prompt, max_tokens=120)

        return {
            "response": answer.strip()
        }

    except Exception as e:
        return {
            "response": "Error generating response",
            "error": str(e)
        }
