from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

tickets_db = []

class Ticket(BaseModel):
    title: str
    description: str
    status: str = "pending"

@router.post("/create")
def create_ticket(ticket: Ticket):
    tickets_db.append(ticket)
    return {"message": "Ticket created"}

@router.get("/all")
def get_tickets():
    return tickets_db
