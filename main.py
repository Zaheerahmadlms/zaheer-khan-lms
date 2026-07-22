from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import datetime
import uuid

app = FastAPI(title="Zaheer Ahmad Khan Advocate - LMS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== MODELS ====================

class Client(BaseModel):
    id: Optional[str] = None
    name: str
    father_name: str
    cnic: str
    phone: str
    whatsapp: str
    email: Optional[str] = None
    address: str
    city: str
    created_at: datetime.datetime = datetime.datetime.now()

class Case(BaseModel):
    id: Optional[str] = None
    case_number: str
    client_id: str
    court: str
    judge: str
    next_hearing: datetime.date
    status: str = "Pending"
    category: str

# In-memory database (baad mein PostgreSQL use karenge)
clients = []
cases = []

@app.get("/")
def home():
    return {
        "message": "Zaheer Ahmad Khan Advocate LMS Backend Running Successfully",
        "version": "1.0"
    }

@app.post("/clients/")
def create_client(client: Client):
    client.id = str(uuid.uuid4())
    clients.append(client)
    return {"status": "success", "client": client}

@app.get("/clients/")
def get_clients():
    return clients

@app.post("/cases/")
def create_case(case: Case):
    case.id = str(uuid.uuid4())
    cases.append(case)
    return {"status": "success", "case": case}

@app.get("/dashboard/")
def dashboard():
    return {
        "todays_hearings": 4,
        "pending_fees": 845000,
        "active_cases": 27,
        "new_clients": 3,
        "notifications": [
            "FIR 302 ka hearing kal hai",
            "Client Ali ka Rs. 50,000 pending hai"
        ]
    }

print("🚀 Zaheer LMS Backend Started - http://127.0.0.1:8000")
