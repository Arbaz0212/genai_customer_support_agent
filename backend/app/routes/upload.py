import os
from fastapi import APIRouter, UploadFile, File
from app.services.document_loader import load_documents

router = APIRouter()

UPLOAD_FOLDER = "documents"

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Reload documents after upload
    load_documents()

    return {"message": "Document uploaded successfully"}
