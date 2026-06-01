from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, HTMLResponse
from pydantic import BaseModel
import uuid
import time
import re
import json
import os
from datetime import datetime

# Upload router
from app.routes.upload import router as upload_router

# RAG service
from app.services.rag import retrieve_context

app = FastAPI(title="AI Customer Support Backend")

# Include upload router
app.include_router(upload_router, prefix="/docs", tags=["Upload"])

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TICKETS_FILE = "tickets.json"


# -------------------------
# Utility: Load tickets safely
# -------------------------
def load_tickets():
    if not os.path.exists(TICKETS_FILE):
        return []

    try:
        with open(TICKETS_FILE, "r") as f:
            data = json.load(f)

            # If file contains dict instead of list, reset it
            if isinstance(data, list):
                return data
            else:
                return []

    except Exception:
        return []


# -------------------------
# Utility: Save tickets safely
# -------------------------
def save_tickets(tickets):
    with open(TICKETS_FILE, "w") as f:
        json.dump(tickets, f, indent=2)


class Query(BaseModel):
    query: str


# -------------------------
# Chat endpoint
# -------------------------
@app.post("/ai/chat")
async def chat(data: Query):

    context = retrieve_context(data.query)

    # ESCALATE if no context found
    if not context:
        return escalate_response(data.query)

    context_lines = context.split("\n")
    query_words = set(data.query.lower().split())

    best_index = None
    best_score = 0

    # Find best matching question
    for i, line in enumerate(context_lines):
        line_words = set(line.lower().split())
        score = len(query_words.intersection(line_words))

        if score > best_score:
            best_score = score
            best_index = i

    if best_index is None or best_score < 2:
        return escalate_response(data.query)

    # Extract answer
    answer_lines = []
    i = best_index + 1

    while i < len(context_lines):
        line = context_lines[i].strip()

        if re.match(r"^\d+\.", line):
            break

        if line:
            answer_lines.append(line)

        i += 1

    if not answer_lines:
        return escalate_response(data.query)

    answer = " ".join(answer_lines).strip()

    def stream_answer():
        for ch in answer:
            yield ch
            time.sleep(0.01)

    return StreamingResponse(stream_answer(), media_type="text/plain")


# -------------------------
# Escalation logic (FIXED)
# -------------------------
def escalate_response(query: str):

    ticket_id = "TKT-" + str(uuid.uuid4())[:8]

    ticket_data = {
        "ticket_id": ticket_id,
        "query": query,
        "status": "Open",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tickets = load_tickets()
    tickets.append(ticket_data)
    save_tickets(tickets)

    def escalate():
        message = (
            "I don't know. Escalating to human agent.\n"
            f"Your support ticket ID: {ticket_id}"
        )
        for ch in message:
            yield ch
            time.sleep(0.01)

    return StreamingResponse(escalate(), media_type="text/plain")


# -------------------------
# ADMIN DASHBOARD
# -------------------------
@app.get("/admin", response_class=HTMLResponse)
def admin_dashboard():
    try:
        with open("app/admin_dashboard.html") as f:
            return f.read()
    except:
        return "<h1>Admin Dashboard File Not Found</h1>"


@app.get("/admin/tickets")
def get_tickets():
    return load_tickets()


@app.post("/admin/tickets/{ticket_id}/resolve")
def resolve_ticket(ticket_id: str):
    tickets = load_tickets()

    for t in tickets:
        if t["ticket_id"] == ticket_id:
            t["status"] = "Resolved"

    save_tickets(tickets)

    return {"status": "resolved"}


@app.delete("/admin/tickets/{ticket_id}/delete")
def delete_ticket(ticket_id: str):
    tickets = load_tickets()

    tickets = [t for t in tickets if t["ticket_id"] != ticket_id]

    save_tickets(tickets)

    return {"status": "deleted"}


# -------------------------
# Health check
# -------------------------
@app.get("/")
def root():
    return {"status": "Backend running successfully"}
