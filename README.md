# 🤖 GenAI Customer Support Agent

> An AI-powered Customer Support Automation Platform built using **FastAPI**, **React**, **RAG (Retrieval-Augmented Generation)**, **FAISS Vector Search**, and **TinyLlama via Ollama** to deliver accurate, context-aware customer support responses while managing support tickets through an integrated admin dashboard.

---

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![RAG](https://img.shields.io/badge/RAG-AI%20Pipeline-orange)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-purple)
![Ollama](https://img.shields.io/badge/Ollama-TinyLlama-black)

---

# 📖 Overview

Customer support teams often spend significant time answering repetitive questions related to refunds, shipping, order tracking, and company policies.

This project solves that problem by implementing a **GenAI-powered Customer Support Agent** capable of:

- Understanding customer queries in natural language
- Retrieving relevant company policies and FAQs using semantic search
- Generating context-aware responses using TinyLlama
- Managing unresolved issues through a ticketing system
- Providing administrators with visibility into customer tickets

Unlike traditional chatbots that rely on keyword matching, this solution uses a **Retrieval-Augmented Generation (RAG)** architecture to ensure responses are grounded in company documentation.

---

# 🚀 Key Features

### AI-Powered Customer Support

- Natural Language Understanding
- Context-Aware Responses
- Semantic Search
- Retrieval-Augmented Generation (RAG)

### Knowledge Base Management

- Upload Support Documents
- Automatic Document Processing
- Text Chunking
- Vector Embedding Generation

### Customer Ticket Management

- Create Tickets
- View Tickets
- Escalate Issues
- Track Ticket Status

### Admin Dashboard

- Monitor Customer Queries
- Review Generated Responses
- Manage Tickets

### Modern Full-Stack Architecture

- React + Vite Frontend
- FastAPI Backend
- FAISS Vector Database
- Ollama Integration

---

# 🏗️ System Architecture

```text
                        ┌──────────────────┐
                        │     Customer     │
                        └─────────┬────────┘
                                  │
                                  ▼
                        ┌──────────────────┐
                        │ React Frontend   │
                        │ (Vite + UI)      │
                        └─────────┬────────┘
                                  │
                                  ▼
                        ┌──────────────────┐
                        │ FastAPI Backend  │
                        └─────────┬────────┘
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
            ▼                     ▼                     ▼
   Ticket Management      Document Retrieval      Upload APIs
            │                     │
            ▼                     ▼
                  ┌─────────────────────────┐
                  │      RAG Pipeline       │
                  └───────────┬─────────────┘
                              │
                              ▼
                     Sentence Transformers
                              │
                              ▼
                        FAISS Search
                              │
                              ▼
                     Relevant Chunks
                              │
                              ▼
                    TinyLlama (Ollama)
                              │
                              ▼
                     AI Generated Reply
```

---

# 🧠 How the AI Pipeline Works

### Step 1: Document Ingestion

Support documents are uploaded into the system.

Examples:

- Refund Policy
- Shipping Policy
- Customer FAQs
- Company Documentation

---

### Step 2: Document Chunking

Large documents are split into smaller chunks for efficient retrieval.

Example:

```text
Refund Policy Document
        ↓

Chunk 1
Chunk 2
Chunk 3
Chunk 4
```

---

### Step 3: Embedding Generation

Each chunk is converted into vector embeddings using:

```text
sentence-transformers
```

Example:

```text
"What is your refund policy?"

↓

[0.23, -0.82, 0.45, ...]
```

---

### Step 4: Vector Storage

Generated embeddings are stored inside:

```text
FAISS Vector Index
```

This enables efficient similarity search.

---

### Step 5: Query Processing

Customer submits a query:

```text
Can I get a refund after 15 days?
```

The query is converted into an embedding.

---

### Step 6: Semantic Retrieval

FAISS retrieves the most relevant document chunks.

Example:

```text
Refund Policy Section
Return Eligibility Section
Cancellation Rules
```

---

### Step 7: Response Generation

Retrieved context is sent to:

```text
TinyLlama (via Ollama)
```

TinyLlama generates a grounded response based on the retrieved knowledge.

---

### Step 8: Response Delivery

The final AI-generated response is returned to the customer through the frontend.

---

# 📁 Project Structure

```text
GenAI_Customer_Support_Agent/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── main.py
│   │   │
│   │   ├── routes/
│   │   │   ├── rag_routes.py
│   │   │   ├── tickets.py
│   │   │   └── upload.py
│   │   │
│   │   ├── services/
│   │   │   ├── rag.py
│   │   │   ├── llm.py
│   │   │   ├── vector_store.py
│   │   │   ├── document_loader.py
│   │   │   └── chunker.py
│   │   │
│   │   ├── utils/
│   │   │   └── utils.py
│   │   │
│   │   ├── data/
│   │   │   ├── docs/
│   │   │   ├── faiss_index/
│   │   │   ├── refund.txt
│   │   │   └── shipping.txt
│   │   │
│   │   ├── admin_dashboard.html
│   │   └── __init__.py
│   │
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── public/
│   │   └── images/
│   │
│   ├── src/
│   │
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── index.html
│
├── tickets.json
│
└── README.md
```

---

# 🛠️ Tech Stack

## Backend

- FastAPI
- Uvicorn
- Python

## AI / GenAI

- TinyLlama
- Ollama
- Transformers
- Torch
- Accelerate

## RAG Components

- Sentence Transformers
- FAISS
- Semantic Search
- Embeddings

## Frontend

- React
- Vite
- Tailwind CSS
- JavaScript

## Data Storage

- JSON-based Ticket Storage
- FAISS Vector Index

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Arbaz0212/genai_customer_support_agent.git

cd genai_customer_support_agent
```

---

# 🐍 Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🦙 Ollama Setup

Install Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

Pull TinyLlama model:

```bash
ollama pull tinyllama
```

Start Ollama server:

```bash
ollama serve
```

Verify model:

```bash
ollama list
```

---

# ▶️ Run Backend

From backend directory:

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```text
http://localhost:8000
```

---

# 💻 Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run development server:

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

# 📡 API Endpoints

## AI Query Endpoint

```http
POST /ask
```

Processes customer questions using RAG.

---

## Upload Documents

```http
POST /upload
```

Uploads support documentation into the knowledge base.

---

## Ticket Management

```http
POST /tickets
GET /tickets
```

Creates and retrieves customer support tickets.

---

# 🎯 Business Impact

This project demonstrates:

- Real-world Generative AI Integration
- Production-style RAG Architecture
- Vector Database Implementation
- Semantic Search Systems
- LLM-Oriented Backend Development
- End-to-End Full-Stack Development
- Customer Support Automation

---

# 🧪 Example Query

Customer:

```text
Can I return a product after 15 days?
```

RAG Pipeline:

```text
Query
↓
Embedding
↓
FAISS Retrieval
↓
Refund Policy Context
↓
TinyLlama
↓
Response
```

AI Response:

```text
According to our refund policy, products can be returned within 30 days of purchase, provided they meet eligibility requirements.
```

---

# 📈 Future Improvements

- PostgreSQL Integration
- User Authentication
- Role-Based Access Control
- Chat History Persistence
- Email Notifications
- WhatsApp Support Integration
- Multi-Language Support
- Analytics Dashboard
- LangGraph Multi-Agent Workflow
- Cloud Deployment

---

# 👨‍💻 Author

**Arbaz**

AI Engineer | Full-Stack Developer | GenAI Enthusiast

GitHub:
https://github.com/Arbaz0212

---

# ⭐ If you found this project useful, consider giving it a star.
